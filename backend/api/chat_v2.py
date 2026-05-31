from fastapi import APIRouter

from schemas.chat_schema import ChatRequest

from llm.llm_manager import llm_response

from rag.memory_manager_v2 import (
    save_message,
    get_conversation
)

router = APIRouter()

MEMORY_WINDOW = 20


@router.post("/chat")
def logic(request: ChatRequest):

    user_message = request.message

    save_message(
        request.session_id,
        "user",
        user_message
    )

    ai_response = llm_response(
    user_message
    )

    save_message(
        request.session_id,
        "assistant",
        ai_response
    )

    return {
        "reply": ai_response
    }


@router.get("/history/{session_id}")
def history(session_id: str):

    history = get_conversation(
        session_id
    )

    return {
        "history": history
    }