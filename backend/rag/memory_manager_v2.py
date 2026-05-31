from database.mongodb import chat_collection


def save_message(
    session_id,
    role,
    message
):

    chat_collection.insert_one(
        {
            "session_id": session_id,
            "role": role,
            "message": message
        }
    )


def get_conversation(
    session_id
):

    messages = chat_collection.find(
        {
            "session_id": session_id
        },
        {
            "_id": 0
        }
    )

    return list(messages)