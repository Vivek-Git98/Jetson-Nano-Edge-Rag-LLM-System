# Jetson Nano Edge RAG LLM System

## Overview

Jetson Nano Edge RAG LLM System is an offline Retrieval-Augmented Generation (RAG) AI assistant optimized for edge deployment on the NVIDIA Jetson Nano.

The project combines:

- Quantized GGUF LLM inference using llama.cpp
- Semantic document retrieval using FAISS
- Embedding-based context search
- FastAPI backend API server
- Streamlit web interface
- Offline inference pipeline
- Edge AI deployment workflow

This system enables local document-aware AI interaction without relying on cloud APIs.

---

# System Architecture

```text
PDF Documents
      ↓
Document Chunking Pipeline
      ↓
Sentence Embeddings
      ↓
FAISS Vector Database
      ↓
Retriever
      ↓
Prompt Builder
      ↓
TinyLlama GGUF (llama.cpp)
      ↓
Generated Response
      ↓
FastAPI Backend
      ↓
Streamlit Frontend
```

---

# Features

- Offline RAG pipeline
- Quantized TinyLlama inference
- GGUF model deployment
- FAISS semantic search
- FastAPI REST API
- Streamlit web interface
- Edge AI compatible
- Jetson Nano optimized workflow
- Multi-document ingestion
- PDF knowledge retrieval
- Local inference without internet

---

# Tech Stack

| Component | Technology |
|---|---|
| LLM | TinyLlama 1.1B |
| Runtime | llama.cpp |
| Quantization | GGUF Q4_K_M |
| Embeddings | sentence-transformers |
| Vector DB | FAISS |
| Backend | FastAPI |
| Frontend | Streamlit |
| Deployment | NVIDIA Jetson Nano |
| Language | Python |

---

# Project Structure

```text
jetson-nano-rag-llm/
│
├── backend/
│   ├── api.py
│   ├── rag_engine.py
│   ├── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│
├── data/
│   ├── raw_docs/
│   ├── processed/
│   │    ├── chunks.pkl
│   │    ├── faiss_index.bin
│   │    ├── texts.pkl
│
├── llama.cpp/
│
├── models/
│   ├── tinyllama-q4.gguf
│
├── scripts/
│   ├── chunk_pipeline.py
│   ├── generate_embeddings.py
│
├── README.md
├── .gitignore
```

---

# Hardware Requirements

## Development PC

Recommended:

- NVIDIA GPU (optional but recommended)
- 16GB RAM
- Python 3.10+
- Windows / Ubuntu

## Deployment Hardware

### NVIDIA Jetson Nano

Recommended configuration:

- Jetson Nano 4GB
- 32GB SD card minimum
- External USB storage recommended
- Ubuntu-based JetPack OS

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <your_repository_url>
cd jetson-nano-rag-llm
```

---

# Python Environment Setup

## Windows

```bash
python -m venv llm_env
llm_env\Scripts\activate
```

## Linux

```bash
python3 -m venv llm_env
source llm_env/bin/activate
```

---

# Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# Install llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

## Build llama.cpp

### Windows

```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

### Linux / Jetson Nano

```bash
cmake -B build
cmake --build build --config Release
```

---

# Model Setup

Place the quantized model:

```text
models/tinyllama-q4.gguf
```

Recommended quantization:

```text
Q4_K_M
```

---

# Document Processing Pipeline

## Step 1 — Add PDFs

Place all PDF documents inside:

```text
data/raw_docs/
```

---

## Step 2 — Run Chunking Pipeline

```bash
python scripts/chunk_pipeline.py
```

---

## Step 3 — Generate Embeddings

```bash
python scripts/generate_embeddings.py
```

This generates:

```text
chunks.pkl
faiss_index.bin
texts.pkl
```

---

# Running Backend API

Go to backend directory:

```bash
cd backend
```

Run:

```bash
uvicorn api:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running Streamlit Frontend

Open a second terminal:

```bash
cd frontend
```

Run:

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# API Example

## POST Request

```json
{
  "question": "What hazards are detected?"
}
```

## Example Response

```json
{
  "question": "What hazards are detected?",
  "answer": "The system detects potholes, rough roads, and speed breakers."
}
```

---

# Quantization Workflow

## Convert HF Model → GGUF

```bash
python convert-hf-to-gguf.py tinyllama_model --outfile tinyllama.gguf
```

## Quantize

```bash
llama-quantize.exe tinyllama.gguf tinyllama-q4.gguf Q4_K_M
```

---

# Running GGUF Model Directly

```bash
llama-cli.exe -m tinyllama-q4.gguf -p "Explain AI"
```

Interactive Chat:

```bash
llama-cli.exe -m tinyllama-q4.gguf -cnv
```

---

# Jetson Nano Deployment

## Install Dependencies

```bash
sudo apt update
sudo apt install build-essential cmake git
```

---

## Build llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release
```

---

## Run Quantized Model

```bash
./build/bin/llama-cli -m tinyllama-q4.gguf -p "Hello"
```

---

# Performance Notes

Expected Jetson Nano performance:

| Metric | Approximate |
|---|---|
| Tokens/sec | 2–5 |
| Model Size | ~636 MB |
| RAM Usage | ~3GB |
| Offline Inference | Supported |

---

# Optimization Recommendations

- Use Q4_K_M quantization
- Limit retrieval chunks to 3–5
- Use USB storage for GGUF models
- Keep prompts concise
- Avoid large context windows

---

# Future Improvements

- Voice assistant integration
- Whisper speech-to-text
- React frontend
- Docker deployment
- CUDA acceleration
- Live document upload
- Chat memory
- Multi-user support
- Agent workflows

---

# Troubleshooting

## GGUF File Not Found

Verify model path:

```text
models/tinyllama-q4.gguf
```

---

## Streamlit Not Opening

Run:

```bash
python -m streamlit run streamlit_app.py
```

---

## FastAPI Connection Errors

Ensure backend is running:

```bash
uvicorn api:app --reload
```

---

# .gitignore

```gitignore
models/
data/
*.gguf
*.bin
*.pkl
__pycache__/
```

---

# License

MIT License

---

# Author

Vivek Kumar

ECE Student | Edge AI | Generative AI | Embedded AI Systems

---

# Acknowledgements

- NVIDIA Jetson Nano
- llama.cpp
- Hugging Face
- FAISS
- Sentence Transformers
- Streamlit
- FastAPI

