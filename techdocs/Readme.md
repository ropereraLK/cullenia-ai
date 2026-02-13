```
                ┌────────────────────────┐
                │     React Frontend     │
                └──────────┬─────────────┘
                           │
                    API Requests
                           │
                ┌──────────▼─────────────┐
                │      FastAPI Backend   │
                └──────────┬─────────────┘
                           │
        ┌──────────────────┼───────────────────┐
        │                  │                   │
┌───────▼─────────┐ ┌──────▼─────────┐ ┌───────▼─────────┐
│ Market Data API │ │ Financial Docs │ │ News & Macro    │
│ (Finnhub etc.)  │ │ (PDF Upload)   │ │ Data APIs       │
└───────┬─────────┘ └──────┬─────────┘ └───────┬─────────┘
        │                  │                   │
        │                  ▼                   │
        │        ┌──────────────────┐          │
        │        │ Document Parsing │          │
        │        └────────┬─────────┘          │
        │                 ▼                    │
        │        ┌──────────────────┐          │
        │        │ Embeddings API   │◄─────────┘
        │        └────────┬─────────┘
        │                 ▼
        │        ┌──────────────────┐
        │        │ Vector Database  │
        │        └────────┬─────────┘
        │                 ▼
        │        ┌──────────────────┐
        │        │   LLM Reasoning  │
        │        └────────┬─────────┘
        │                 ▼
        └────────────► Structured Insights
```

## 1. Frontend Layer (React)

### Purpose

The frontend provides an interactive interface for users to:

- Upload financial reports
- View analysis dashboards
- Compare companies across markets
- Ask AI-powered financial questions

### Why React?

- Industry-standard frontend framework
- Strong ecosystem for financial charting
- Component-based architecture
- Scalable and production-ready

The frontend focuses purely on visualization and user interaction, keeping AI and data processing logic in the backend.

---

## 2. Backend Layer (FastAPI)

### Purpose

The backend acts as the orchestration layer and is responsible for:

- Coordinating AI services
- Calling external financial data APIs
- Storing structured and unstructured data
- Managing vector search operations
- Combining numeric financial metrics with AI reasoning

### Why FastAPI?

- Lightweight and high performance
- Easy integration with AI APIs
- Asynchronous support for external calls
- Production-ready architecture

FastAPI ensures clean separation between user interaction and AI/data logic.

---

## 3. Market Data Layer

### Data Sources

- Finnhub
- Alpha Vantage
- IEX Cloud

### Purpose

This layer retrieves structured market data including:

- Historical price data
- Volatility metrics
- Liquidity indicators
- Order book depth

There is no model training at this stage — this layer focuses on reliable and structured data retrieval.

---

## 4. Financial Document Intelligence Layer

### User Inputs

- Annual report PDFs
- Interim financial reports

### System Process

1. Extract text from PDF
2. Split content into structured chunks
3. Generate embeddings
4. Store embeddings in vector database

### Why?

This enables the system to answer contextual financial questions such as:

“What are the main risks mentioned in this company’s annual report?”

This architecture follows the Retrieval-Augmented Generation (RAG) pattern.

No model training is required.

---

## 5. Embeddings + Vector Database Layer

### Tools

- OpenAI Embeddings
- Pinecone / FAISS / Supabase Vector

### Purpose

This layer enables:

- Semantic document search
- Context retrieval
- Intelligent lookup of financial disclosures

It allows the LLM to reason over relevant financial content rather than relying on generic knowledge.

This approach reflects modern enterprise AI architecture.

---

## 6. LLM Reasoning Layer

### Tools

- OpenAI GPT
- Claude

### Responsibilities

This layer:

- Summarizes financial statements
- Explains valuation gaps
- Interprets volatility spikes
- Compares SGX vs CSE companies
- Converts structured financial metrics into readable insights

### Important Principle

The system does not attempt deterministic prediction.

Instead, it performs reasoning over structured financial data to generate explainable and contextual analysis.

This design improves reliability and reduces instability.

---

## 7. Financial Logic Layer (Non-AI, Critical)

Before sending information to the LLM, the system computes structured financial metrics such as:

- Return on Equity (ROE)
- Return on Assets (ROA)
- Debt-to-Equity Ratio
- Revenue Growth Rate
- Volatility Measures
- Sharpe Ratio (optional)

These computed metrics are passed to the LLM as structured inputs.

### Why This Matters

Providing structured numerical context:

- Reduces hallucination risk
- Improves financial accuracy
- Ensures grounded reasoning
- Enhances explainability

The LLM acts as a reasoning and interpretation engine, not a replacement for financial computation.

---

## Architectural Philosophy

Cullenia.ai follows these core principles:

- No heavy model training
- AI as a service integration
- Structured financial grounding
- Explainable outputs
- Clear separation of concerns
- Production-aligned architecture

This design ensures scalability, maintainability, and real-world applicability without infrastructure complexity.

## RAG Architecture

<p align="Left">
  <img src="assets/docs/RAG_Suggested_Model.png"/>
</p>