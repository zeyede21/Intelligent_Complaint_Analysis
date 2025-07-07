import streamlit as st
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from rag_task3 import retrieve_and_answer  # Uses question param, not query

# Load vector store
faiss_index = faiss.read_index("../vector_store/faiss_index.index")
with open("../vector_store/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
with open("../vector_store/chunk_metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Load embedder
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Streamlit UI
st.set_page_config(page_title="CrediTrust Complaint Chatbot", layout="wide")
st.title("📊 CrediTrust Complaint Insight Assistant")

# Input
query = st.text_input("Ask a question about customer complaints:", "")

if st.button("Submit") and query:
    with st.spinner("Analyzing complaints..."):
        # ✅ Fix: pass query as positional or as `question=`
        answer, retrieved_chunks = retrieve_and_answer(query)

    st.markdown("### 🤖 Answer")
    st.success(answer)

    st.markdown("### 🧾 Sources")
    for i, src in enumerate(retrieved_chunks):
        st.markdown(f"**Source {i+1}:**")
        st.info(src)

if st.button("Clear"):
    st.experimental_rerun()
