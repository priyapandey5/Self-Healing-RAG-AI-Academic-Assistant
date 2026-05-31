from fastapi import APIRouter

from schemas.chat_schema import ChatRequest
from llm.llm_manager import llm_response
from rag.memory_manager import save_message


router = APIRouter()


@router.post("/chat")
def logic(request: ChatRequest):

    user_message = request.message

    # Save user message
    save_message(
        request.session_id,
        "user",
        user_message
    )

    # ✅ FIX: removed session_id from llm_response
    ai_response = llm_response(user_message)

    # Save AI response
    save_message(
        request.session_id,
        "assistant",
        ai_response
    )

    return {
        "reply": ai_response
    }