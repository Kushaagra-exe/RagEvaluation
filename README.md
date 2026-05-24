<div align="center">


# RAG Evaluation  System
</div>

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

This is a sample approach to improve Retrieval - Various different techniques can be added to perform the RAG Evaluations

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


| Metric             | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| Euclidean Distance | Measures embedding-level similarity between query and retrieved documents                     |
| Faithfulness       | Measures factual consistency of generated answers with retrieved context                      |
| Answer Relevancy   | Measures how relevant the generated answer is to the user query                               |
| Context Precision  | Measures how much of the retrieved context is relevant                                        |
| Context Recall     | Measures whether important information was successfully retrieved                             |
| Answer Correctness | Measures similarity between generated answer and ground truth                                 |
| Recall@K           | Measures how many of the total relevant retrieved contexts appear in the top K results        |
| Precision@K        | Measures how many of the top K retrieved contexts are actually relevant                       |
| MRR                | Measures how early the first relevant context appears in the ranked retrieval results         |
| NDCG@K             | Measures ranking quality by rewarding relevant contexts appearing higher in the top K results |


# Project Structure

```text

  ├── README.md
  ├── answers.json
  ├── benchmark.md
  ├── benchmarks.json
  ├── compare.py
  ├── Quantum computing.txt
  ├── RAGeval.py
  ├── strategy_a.json
  ├── strategy_b.json
  ├── synthetic_generation.py
  ├── validation.json
  ├── VectorRetrievalEval.py
  ├── pipelines/
  │   ├── rag.py
  │   ├── retievalmetrics.py
  │   ├── retrieval_pipeline.py
  │   └── synthetic_pipeline.py
  └── utils/
      ├── helper.py
      ├── QueryExpander.py
      ├── structure.py
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
### `VectorRetrievalEval.py`

Compares the performance of both retrieval strategies on basis of The Syntactic Metrics.

Compares Vector Retrieval on following Metrics:
- Recall@K
- Precision@K
- MRR
- NDCG@K

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

## 5. Run RAG Evaluation

```bash
python RAGeval.py
```

---

## 6. Compare Strategies

```bash
python compare.py
```

## 7. Run Vector Db Retrieval Evaluation

```bash
python VectorRetrievalEval.py
```
# Author

**Kushaagra Mehta**  