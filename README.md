# 🎓 Self-Healing-RAG AI Academic Assistant

An intelligent Retrieval-Augmented Generation (RAG) chatbot capable of automatically correcting failed retrieval attempts using an AI Critic Agent before generating the final response.

Unlike traditional RAG systems, this project introduces a **Self-Healing Retrieval Pipeline**, where an LLM Critic evaluates generated answers and rewrites the user query whenever retrieval quality is insufficient.

---
<img width="1920" height="831" alt="Screenshot 2026-07-23 080358" src="https://github.com/user-attachments/assets/02fc848b-f62f-4e6e-937c-31438feff77f" />
<img width="1920" height="857" alt="Screenshot 2026-07-23 080443" src="https://github.com/user-attachments/assets/ece7c5d9-ff76-4662-b372-02421e5f0b25" />


# 🚀 Features

## ✅ Retrieval-Augmented Generation (RAG)

- Document-based Question Answering
- Context-aware responses
- Semantic Search using FAISS
- Sentence Transformer Embeddings

---

## 🤖 Self-Healing Retrieval

The most important feature of this project.

Instead of immediately responding when retrieval fails:

User Question

↓

Retriever

↓

Generator

↓

Critic Agent

↓

If Context is Poor

↓

Rewrite Query

↓

Retrieve Again

↓

Generate Better Answer

This significantly improves answer quality without requiring the user to rephrase their question.

---

## 🧠 AI Agents

### Generator Agent

Responsible for generating the final response from retrieved context.

### Critic Agent

Responsible for:

- Evaluating generated answers
- Detecting weak retrieval
- Suggesting improved search queries
- Triggering another retrieval cycle

---

## 💾 Chat Memory

Maintains conversation history using session IDs.

Supports:

- Multiple conversations
- Context preservation
- History retrieval

---

## 📂 Document Upload

Users can upload academic PDFs.

The system automatically:

- Extracts text
- Splits into chunks
- Generates embeddings
- Updates the FAISS vector database

No manual preprocessing required.

---

## 🎨 Modern Streamlit Interface

Features:

- ChatGPT-like interface
- Academic sidebar
- Conversation history
- Source display
- Loading indicators
- Backend status monitoring

---

# 🏗 Project Architecture

```

```
                +----------------------+
                |   Streamlit UI       |
                +----------+-----------+
                           |
                           |
                    POST /chat
                           |
                           ▼
                +----------------------+
                |    FastAPI Backend   |
                +----------+-----------+
                           |
             +-------------+-------------+
             |                           |
             ▼                           ▼
      Memory Manager              Document Upload
             |                           |
             ▼                           ▼
       Conversation              PDF Processing
                                      |
                                      ▼
                             Text Chunking
                                      |
                                      ▼
                            Sentence Transformer
                                      |
                                      ▼
                                   FAISS
                                      |
                                      ▼
                               Retriever
                                      |
                                      ▼
                            Generator Agent
                                      |
                                      ▼
                              Critic Agent
                                      |
             +------------------------+
             |
     Query Approved?
      /           \
    Yes            No
    |               |
    ▼               ▼
Return Answer   Rewrite Query
                    |
                    ▼
              Retrieve Again
```

---

# 📁 Project Structure

```
Self-Healing-RAG/
│
├── backend/
│   ├── api/
│   │   ├── chat_v2.py
│   │   └── upload_v3.py
│   │
│   ├── core/
│   │   └── prompts.py
│   │
│   ├── llm/
│   │   ├── gemini_client.py
│   │   ├── generator.py
│   │   ├── critic.py
│   │   └── llm_manager.py
│   │
│   ├── rag/
│   │   ├── embedder.py
│   │   ├── retriever.py
│   │   ├── faiss_store.py
│   │   ├── pipeline.py
│   │   ├── memory_manager_v2.py
│   │   └── text_chunker.py
│   │
│   ├── schemas/
│   │   └── chat_schema.py
│   │
│   ├── utils/
│   │   └── pdf_loader.py
│   │
│   ├── uploads/
│   ├── data/
│   └── main_v3.py
│
├── frontend/
│   ├── UI_v2.py
│   └── requirements.txt
│
├── README.md
└── requirements.txt
```

---

# ⚙ Tech Stack

## Backend

- FastAPI
- Uvicorn
- Python

## Frontend

- Streamlit

## Vector Database

- FAISS

## Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

## LLM

- Google Gemini 2.5 Flash

## AI Components

- Generator Agent
- Critic Agent

## PDF Processing

- PyPDF

---

# 🔄 Self-Healing Workflow

### Step 1

User asks a question.

↓

### Step 2

Retriever searches the vector database.

↓

### Step 3

Generator creates an answer.

↓

### Step 4

Critic evaluates:

- Is context sufficient?
- Is answer relevant?
- Can retrieval improve?

↓

### Step 5

If retrieval is weak:

Critic rewrites the query.

↓

### Step 6

Retriever searches again.

↓

### Step 7

Generator creates improved answer.

↓

### Final Response

Returned with document sources.

---

# 📄 Source Attribution

Every generated response includes the documents used during retrieval.

Example:

```
📄 Sources

• Admissions Handbook.pdf

• Fee Structure.pdf

• Academic Calendar.pdf
```

---

# 🌟 Example Questions

## Admissions

- What documents are required for admission?
- What is the admission process?

## Fees

- What is the JEE fee?
- What is the NEET fee?

## Faculty

- Who teaches Physics?
- Show faculty details.

## Academic Calendar

- When do classes start?
- Show semester schedule.

## Study Material

- Do you provide study material?
- What books are recommended?

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/<username>/Self-Healing-RAG.git

cd Self-Healing-RAG
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main_v3:app --reload
```

Runs at

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

pip install -r requirements.txt

streamlit run UI_v2.py
```

Runs at

```
http://localhost:8501
```

---

# ☁ Deployment

## Backend

Deployed on Railway

FastAPI + Uvicorn

---

## Frontend

Deployed on Railway

Streamlit

---

# 🎯 Future Improvements

- Multi-user Authentication
- OCR Support
- Image-based Queries
- Voice Input
- Streaming Responses
- Hybrid Retrieval
- Metadata Filtering
- Conversation Summarization

---

# 👩‍💻 Author

**Priya Pandey**

Master of Computer Applications (2024–2026)

United Institute of Management

Passionate about

- Artificial Intelligence
- Retrieval-Augmented Generation
- Large Language Models
- Agentic AI
- Full Stack Development

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.
