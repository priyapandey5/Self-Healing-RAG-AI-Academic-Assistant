# models/chat_history.py

from database.mongo import chat_collection


def save_chat(session_id, question, answer):

    chat_collection.insert_one(
        {
            "session_id": session_id,
            "question": question,
            "answer": answer
        }
    )