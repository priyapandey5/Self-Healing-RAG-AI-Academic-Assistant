from fastapi import FastAPI

from api.chat_v2 import router as chat_router
from api.upload_v3 import router as upload_router

app = FastAPI(
    title="RAG Chatbot API",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


app.include_router(chat_router)
app.include_router(upload_router)
