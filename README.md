# 🧠 Intelligent Complaint Analysis for Financial Services

_A Retrieval-Augmented Generation (RAG) Chatbot for CrediTrust Financial_

## 📌 Project Overview

CrediTrust Financial receives thousands of customer complaints across five financial product lines. This project builds an internal **AI-powered assistant** using **Retrieval-Augmented Generation (RAG)** to help internal teams extract insights from unstructured complaint narratives.

With this tool, non-technical users like product managers and compliance officers can ask natural-language questions (e.g., _“Why are users unhappy with BNPL?”_) and instantly receive evidence-backed answers with context.

---

## 🚀 Key Features

✅ Load and clean thousands of real-world complaints  
✅ Embed and store them using a vector database (FAISS)  
✅ Query relevant chunks via semantic search  
✅ Feed them to a language model (LLM) to generate insights  
✅ Serve it all through a simple, interactive Streamlit UI

---

## 🧩 Project Structure

Intelligent_Complaint_Analysis/
├── data/
│ └── processed/filtered_complaints.csv
├── notebooks/
│ ├── task1_eda_preprocessing.ipynb
│ └── task2_chunking_embedding.ipynb
├── src/
│ ├── rag_task3.py # RAG pipeline + evaluation
│ └── app.py # Streamlit UI
├── vector_store/
│ ├── faiss_index.index
│ ├── chunk_metadata.pkl
│ └── chunks.pkl
├── .gitignore
├── README.md
└── requirements.txt

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/Intelligent_Complaint_Analysis.git
cd Intelligent_Complaint_Analysis

# 2. Create a virtual environment
python -m venv myenvv
source myenvv/bin/activate  # or .\myenvv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run preprocessing and vector store creation (Tasks 1 & 2)
# Or review notebooks in /notebooks/

# 5. Run the RAG pipeline (Task 3 - evaluation)
python src/rag_task3.py

# 6. Launch the Streamlit app (Task 4)
streamlit run src/app.py
```
