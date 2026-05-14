# RAG Evaluation & Query Retrieval Benchmarking System

## Overview

This project is a comprehensive **Retrieval-Augmented Generation (RAG) Evaluation Framework** designed to benchmark and compare different retrieval strategies for question-answering systems.

The system evaluates how effectively different retrieval approaches fetch relevant context documents and how accurately the generated answers align with the ground truth using industry-standard evaluation metrics.

The project focuses on comparing two retrieval strategies:

1. **Simple Retrieval**
  - Direct semantic search using vector similarity.
2. **Query Expansion + Retrieval**
  - Expands the original user query using an LLM before retrieval to improve contextual search quality.

The framework also supports:

- Synthetic dataset generation
- Automated benchmarking
- Retrieval quality analysis
- RAG response evaluation using RAGAS
- Euclidean distance comparison between retrieved embeddings

---

# Key Features

- Semantic Retrieval using Vector Databases
- Query Expansion for Enhanced Retrieval
- Synthetic Validation Dataset Generation
- RAG Pipeline Evaluation
- Automated Benchmark Reporting
- Multi-Metric Evaluation using RAGAS
- Ground Truth Generation
- Euclidean Distance Analysis of Retrieved Documents
- Modular & Extensible Architecture

---

# Retrieval Strategies

## Strategy A — Simple Retrieval

This strategy performs:

1. Query embedding generation
2. Vector similarity search
3. Retrieval of top-k relevant documents

It serves as the baseline retrieval pipeline.

---

## Strategy B — Query Expansion + Retrieval

This strategy:

1. Expands the original query using an LLM
2. Generates semantically richer search queries
3. Performs retrieval using expanded queries
4. Aggregates and ranks the retrieved documents

This approach improves:

- Semantic coverage
- Context diversity
- Retrieval recall
- Answer grounding

---

# Evaluation Metrics

The framework evaluates both retrieval quality and answer quality using the following metrics:


| Metric             | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Euclidean Distance | Measures embedding-level similarity between query and retrieved documents |
| Faithfulness       | Measures factual consistency of generated answers with retrieved context  |
| Answer Relevancy   | Measures how relevant the generated answer is to the user query           |
| Context Precision  | Measures how much of the retrieved context is relevant                    |
| Context Recall     | Measures whether important information was successfully retrieved         |
| Answer Correctness | Measures similarity between generated answer and ground truth             |


---

# More Evaluation Metrics (future)

## Recall@K
Precision@K
MRR
NDCG@K

# Project Structure

```text
kushaagra-exe-ragevaluation/
│
├── answers.json
├── benchmark.md
├── benchmarks.json
├── compare.py
├── helper.py
├── Quantum computing.txt
├── QueryExpander.py
├── rag.py
├── RAGeval.py
├── retrieval_pipeline.py
├── strategy_a.json
├── strategy_b.json
├── structure.py
├── synthetic_generation.py
├── synthetic_pipeline.py
├── validation.json
└── vectorstore.py
```

---

# Workflow Architecture

```text
                 ┌────────────────────┐
                 │ Source Documents   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Vector Store       │
                 │ (Embeddings/FAISS) │
                 └─────────┬──────────┘
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
 ┌──────────────────┐             ┌────────────────────┐
 │ Strategy A       │             │ Strategy B         │
 │ Simple Retrieval │             │ Query Expansion    │
 └────────┬─────────┘             └─────────┬──────────┘
          │                                 │
          ▼                                 ▼
   Retrieved Docs                    Expanded Retrieval
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                ┌────────────────┐
                │ RAG Generation │
                └───────┬────────┘
                        ▼
                ┌────────────────┐
                │ RAGAS Eval     │
                └───────┬────────┘
                        ▼
                ┌────────────────┐
                │ Benchmarking   │
                └────────────────┘
```

---
# File-by-File Explanation

## Core Retrieval Components

### `QueryExpander.py`

Responsible for expanding user queries before retrieval.

Functions:

- Uses an LLM to generate semantically related query variants
- Improves retrieval recall
- Helps fetch broader contextual information
- Used in Strategy B

Example:

```text
Original Query:
"What are applications of quantum computing?"

Expanded Queries:
- Uses of quantum computing
- Real world applications of quantum computers
- Quantum computing industry applications
```

---

### `helper.py`

Provides utility functions and shared resources used throughout the project.

Includes:

- LLM initialization
- Embedding model initialization
- Retriever setup
- Data ingestion utilities
- Common helper methods

Acts as the central utility module for the framework.

---

### `vectorstore.py`

Handles:

- Vector database initialization
- Document chunking
- Embedding generation
- Storage of documents into the vector database

Responsibilities:

1. Read source documents
2. Generate embeddings
3. Store embeddings in FAISS/vector store
4. Enable semantic similarity retrieval

---

### `retrieval_pipeline.py`

Implements the document retrieval workflow.

Contains:

- Retrieval logic
- Similarity search
- Top-k retrieval
- Retrieval ranking mechanisms

Used internally by the RAG pipeline.

---

### `rag.py`

Main RAG orchestration pipeline.

Handles:

- Query processing
- Retrieval using both strategies
- Context generation
- Answer generation using LLMs
- Final response formatting

Supports:

- Strategy A (Simple Retrieval)
- Strategy B (Query Expansion Retrieval)

---

## Evaluation Components

### `RAGeval.py`

Performs automated RAG evaluation using the RAGAS framework.

Evaluates:

- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall
- Answer Correctness

This module generates benchmark reports for both retrieval strategies.

---

### `compare.py`

Compares the performance of both retrieval strategies.

Used for:

- Strategy-wise metric comparison
- Euclidean distance analysis
- Benchmark summarization

Helps identify which retrieval approach performs better.

---

## Synthetic Dataset Generation

### `synthetic_generation.py`

Generates synthetic validation questions and answers from source documents.

Used to:

- Create evaluation datasets automatically
- Generate realistic QA pairs
- Reduce manual annotation effort

---

### `synthetic_pipeline.py`

Pipeline that orchestrates synthetic data generation.

Handles:

1. Reading documents
2. Generating synthetic queries
3. Creating ground truth answers
4. Saving evaluation datasets

---

## Data Structures

### `structure.py`

Contains structured schemas and output formats.

Used for:

- Typed outputs
- Response schemas
- Consistent formatting across modules

---

# Dataset & Source Files

### `Quantum computing.txt`

Primary knowledge source used for:

- Vector embedding generation
- Retrieval
- Synthetic dataset creation
- Evaluation benchmarking

---

# Output Files

## `benchmark.md`

Contains the final benchmark report.

Includes:

- Euclidean distance comparisons
- Faithfulness scores
- Answer relevancy scores
- Context precision scores
- Context recall scores
- Answer correctness scores
- Strategy-wise performance analysis

This is the primary evaluation report.

---

## `validation.json`

Synthetic validation dataset generated from source documents.

Contains:

- Questions
- Ground truth answers
- Validation samples for benchmarking

---

## `benchmarks.json`

Stores retrieved documents and evaluation outputs from both retrieval strategies.

Used for:

- Analysis
- Debugging
- Metric computation

---

## `answers.json`

Contains:

- Ground truth answers
- Expected outputs for evaluation

Used during RAGAS benchmarking.

---

## `strategy_a.json`

Stores outputs from:

- Simple retrieval strategy

Includes:

- Retrieved contexts
- Generated answers
- Retrieval metadata

---

## `strategy_b.json`

Stores outputs from:

- Query expansion retrieval strategy

Includes:

- Expanded queries
- Retrieved contexts
- Generated answers
- Retrieval metadata

---

# Technologies Used


| Category      | Technology            |
| ------------- | --------------------- |
| Language      | Python                |
| Vector Store  | FAISS                 |
| LLM Framework | LangChain             |
| Evaluation    | RAGAS                 |
| Embeddings    | Sentence Transformers |
| Retrieval     | Semantic Search       |
| Data Handling | JSON                  |
| Synthetic QA  | LLM-based Generation  |


---

# Use Cases

This framework can be used for:

- Evaluating enterprise RAG systems
- Benchmarking retrieval strategies
- Improving semantic search pipelines
- Research in information retrieval
- Testing query expansion techniques
- LLM grounding analysis
- Academic and industrial AI projects

---

# How to Run

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

---

## 3. Generate Synthetic Validation Data

```bash
python synthetic_pipeline.py
```

---

## 4. Run Retrieval Pipelines

```bash
python retrieval_pipeline.py
```

---

## 5. Run Evaluation

```bash
python RAGeval.py
```

---

## 6. Compare Strategies

```bash
python compare.py
```

---

# Future Improvements

Potential enhancements:

- Recall@K
- Precision@K
- MRR
- NDCG@K

---

# Author

**Kushaagra Mehta**  