from database.mongodb import chat_collection

chat_collection.insert_one(
    {
        "session_id": "test",
        "role": "user",
        "message": "hello mongodb"
    }
)

print("Inserted Successfully")