from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["rag_assistant"]

chat_collection = db["chat_history"]