<p align="center">
  <img src="assets/logo.png" alt="Cullenia.ai Logo" width="300"/>
</p>

<h1 align="center">Cullenia.ai</h1>

<p align="center">
  AI-driven financial statement and stock market analysis platform
</p>

# Cullenia AI - FastAPI Application

A FastAPI-based Python application for Cullenia AI.

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at:
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

## Project Structure

```
cullenia-ai/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Development

To run with auto-reload (development mode):
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Production

For production deployment, use:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
Designed and implemented an AI-driven framework to compare emerging and developed stock markets (CSE vs SGX)

Built end-to-end data pipelines using financial APIs and public company filings

Engineered financial, technical, and volatility-based features for machine learning models

Applied supervised ML models to identify market trends and profitability patterns

Integrated explainable AI (SHAP) to interpret model predictions

Implemented Retrieval-Augmented Generation (RAG) to extract insights from financial documents

Developed interactive dashboards using React for visualization
```
