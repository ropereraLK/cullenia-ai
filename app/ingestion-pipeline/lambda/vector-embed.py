import json
import boto3
import pdfplumber
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

region = "ap-south-1"

s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime", region_name=region)

# Auth for OpenSearch
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    "es",
    session_token=credentials.token
)

opensearch = OpenSearch(
    hosts=[{"host": "YOUR_HOST", "port": 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

INDEX_NAME = "documents"


def lambda_handler(event, context):
    try:
        record = event["Records"][0]
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        print(f"Processing file: {key}")

        file_obj = s3.get_object(Bucket=bucket, Key=key)

        text = extract_text(file_obj["Body"])
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)

            doc = {
                "text": chunk,
                "embedding": embedding,
                "source": key,
                "chunk_id": i
            }

            opensearch.index(index=INDEX_NAME, body=doc)

        return {"status": "success"}

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e


# ----------------------------
# Extract text from PDF
# ----------------------------
def extract_text(file_stream):
    text = ""
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# ----------------------------
# Chunking
# ----------------------------
def chunk_text(text, size=500, overlap=100):
    words = text.split()
    chunks = []

    for i in range(0, len(words), size - overlap):
        chunk = " ".join(words[i:i + size])
        chunks.append(chunk)

    return chunks


# ----------------------------
# Bedrock Embedding
# ----------------------------
def get_embedding(text):
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v1",
        body=json.dumps({"inputText": text})
    )

    result = json.loads(response["body"].read())
    return result["embedding"]