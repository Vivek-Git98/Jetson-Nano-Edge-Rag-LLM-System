import pickle
import numpy as np
import faiss
import subprocess

from sentence_transformers import SentenceTransformer

# =========================================
# LOAD VECTOR DATABASE
# =========================================

index = faiss.read_index(
    r"D:\llm fine tuning\data\processed\faiss_index.bin"
)

with open(r"D:\llm fine tuning\data\processed\texts.pkl", "rb") as f:
    texts = pickle.load(f)

print(f"Loaded {len(texts)} chunks")

# =========================================
# LOAD EMBEDDING MODEL
# =========================================

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded")

# =========================================
# RETRIEVAL FUNCTION
# =========================================

def retrieve(query, k=5):

    query_embedding = embed_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    D, I = index.search(query_embedding, k)

    results = [texts[i] for i in I[0]]

    return results

# =========================================
# PROMPT BUILDER
# =========================================

def build_prompt(query, context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a technical assistant.

STRICT RULES:
- Answer ONLY using the provided context
- Do NOT hallucinate
- If answer not found, say "Not found in document"
- Keep answers concise and technical

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt

# =========================================
# GGUF MODEL INFERENCE
# =========================================

def generate_answer(prompt):

    llama_cli = (
        r"D:\llm fine tuning\llama.cpp\build\bin\Release\llama-cli.exe"
    )

    model_path = (
        r"D:\llm fine tuning\llama.cpp\build\bin\Release\tinyllama-q4.gguf"
    )

    cmd = [
        llama_cli,
        "-m", model_path,
        "-p", prompt,
        "-n", "120",
        "--temp", "0.3"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    print("\n========== STDOUT ==========\n")
    print(result.stdout)

    print("\n========== STDERR ==========\n")
    print(result.stderr)

    output = result.stdout

    # Extract answer cleanly
    if "Answer:" in output:
        output = output.split("Answer:")[-1]

    output = output.strip()

    if len(output) < 5:
        output = "No valid response generated."

    return output

# =========================================
# COMPLETE RAG PIPELINE
# =========================================

def ask_query(query):

    print(f"\nUser Query: {query}")

    context_chunks = retrieve(query)

    prompt = build_prompt(query, context_chunks)

    answer = generate_answer(prompt)

    return answer