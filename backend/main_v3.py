from fastapi import FastAPI

from api.chat_v2 import router as chat_router
from api.upload_v3 import router as upload_router

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)


# -------------------------
# ROOT ROUTE
# Railway Health Check
# -------------------------
@app.get("/")
def root():
    return {
        "status": "healthy",
        "message": "RAG Chatbot API is running"
    }


# -------------------------
# HEALTHCHECK ROUTE
# -------------------------
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -------------------------
# API ROUTES
# -------------------------
app.include_router(chat_router)
app.include_router(upload_router)
