import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from huggingface_hub import login

# Authenticate (⚠️ Avoid hardcoding tokens in production!)
login(token="mytoken")

# ---------------------------
# Load Vector Store & Metadata
# ---------------------------
index = faiss.read_index(r"D:\10Academy1\Intelligent_Complaint_Analysis\vector_store\faiss_index.index")

with open(r"D:\10Academy1\Intelligent_Complaint_Analysis\vector_store\chunk_metadata.pkl", "rb") as f:
    metadatas = pickle.load(f)

with open(r"D:\10Academy1\Intelligent_Complaint_Analysis\vector_store\chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print(f"[INFO] Vector store loaded: {index.ntotal} vectors")
print(f"[INFO] Metadata and chunks loaded: {len(metadatas)} entries")

# ---------------------------
# Initialize Embedding & LLM
# ---------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
llm = pipeline("text2text-generation", model="google/flan-t5-base")
print("[INFO] Embedding model and LLM pipeline initialized")

# ---------------------------
# Prompt Template
# ---------------------------
prompt_template = (
    "You are a financial analyst assistant for CrediTrust.\n"
    "Your task is to answer questions about customer complaints.\n"
    "Use the following retrieved complaint excerpts to formulate your answer.\n"
    "If the context doesn't contain the answer, say you don't have enough information.\n"
    "\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
)

# ---------------------------
# Retrieval + Generation Function
# ---------------------------
def retrieve_and_answer(question, k=5):
    print(f"\n[QUESTION] {question}")

    # Embed question
    question_embedding = embedding_model.encode([question])
    print(f"[INFO] Question embedded. Shape: {question_embedding.shape}")

    # Search similar chunks
    distances, indices = index.search(question_embedding, k)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    print(f"[INFO] Retrieved {len(retrieved_chunks)} chunks")

    # Show preview of first chunk
    if retrieved_chunks:
        print(f"[DEBUG] First retrieved chunk:\n{retrieved_chunks[0][:300]}...\n")

    # Build prompt
    context = "\n---\n".join(retrieved_chunks)
    prompt = prompt_template.format(context=context, question=question)
    print(f"[DEBUG] Prompt sent to LLM (truncated):\n{prompt[:700]}...\n")

    # Generate answer
    response = llm(prompt, max_new_tokens=250, do_sample=True, top_k=5)[0]['generated_text']
    answer = response.split("Answer:")[-1].strip()

    print(f"[INFO] LLM Answer:\n{answer}\n")
    return answer, retrieved_chunks

# ---------------------------
# Evaluation Logic
# ---------------------------
example_questions = [
    "Why are users unhappy with Buy Now, Pay Later?",
    "What common issues do customers report for credit cards?",
    "Are there complaints about money transfer delays?",
    "What are the main pain points for personal loan customers?",
    "Do customers mention fraud in savings accounts?",
]

print("\n===== RAG Evaluation Results =====\n")
for q in example_questions:
    answer, sources = retrieve_and_answer(q)
    print("Top Sources:")
    for src in sources[:2]:
        print(f"- {src[:200]}...")
    print("\nScore (1-5): __  Comments: __\n")
