# AI Context Engine

A context-aware backend intelligence system that surfaces system state, dependencies, and risks from existing data - reducing the need for manual discussions and accelerating decision-making.

---

## Screenshots Demo

 

![alt text](image.png)

  

---

## What This Project Solves

Understanding a system usually requires:

* Reading scattered documentation
* Asking multiple developers
* Exploring code manually

This system eliminates that overhead by:

* Retrieving relevant context automatically
* Structuring it into actionable insights
* Providing instant system-level understanding

---

## Features

* Document ingestion and intelligent chunking
* Semantic embeddings using HuggingFace
* Scalable vector storage with Pinecone
* Context-aware retrieval (top-k similarity search)
* LLM-powered reasoning
* Structured output using Pydantic

---

## Tech Stack

* Python
* LangChain (LCEL pipelines)
* HuggingFace (LLM + Embeddings)
* Pinecone (Vector Database)
* Pydantic (Structured output)

---

## Project Structure

```
app/
 ├── models/          # Output schema (Pydantic)
 ├── prompts/         # Prompt templates
 ├── embeddings/      # Embedding model
 ├── vectorstore/     # Pinecone setup
 ├── retriever/       # Retrieval logic
 ├── chains/          # RAG pipeline (LCEL)
 ├── services/        # Business logic layer
 ├── loaders/         # Document loader
 ├── splitters/       # Text chunking
 ├── main.py          # CLI interface
 ├── ingest.py        # Data ingestion pipeline
```

---

## How It Works

```
Documents → Embeddings → Pinecone  
                        ↓
User Query → Retriever → Context → LLM → Structured Output
```

---

## Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Configure environment variables

```
HUGGINGFACEHUB_API_TOKEN=your_token
PINECONE_API_KEY=your_key
```

---

## Run

### Step 1: Ingest data into vector DB

```
python app/ingest.py
```

### Step 2: Start the application

```
python app/main.py
```

---

## Example Query

```
What is the status of authentication?
```

---

## Output

* Summary
* Dependencies
* Risks

---

## Key Design Decisions

* Separation of ingestion and query pipelines
* Modular architecture (retriever, chain, service layers)
* Structured output using schema validation
* Scalable vector search using Pinecone

---

## Notes

* Embedding dimension must match Pinecone index
* Ingestion must be run before querying
* Output reliability depends on document quality

---

## Future Improvements

* FastAPI backend for production use
* Agent-based workflows (tool calling)
* Hybrid search (keyword + vector)
* Query classification and routing

---
