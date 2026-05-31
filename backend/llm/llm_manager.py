from llm.gemini_client import client
from core.prompts import system_prompt
from rag.retriever import retrieve_chunks


def llm_response(query, conversation=None):

    similar_chunks = retrieve_chunks(query)

    context = "\n\n".join(
        similar_chunks
    )

    print("\n===== RETRIEVED CONTEXT =====")
    print(context)
    print("============================\n")

    prompt = (
        system_prompt
        + "\n\nContext:\n"
        + context
        + "\n\nUser Question:\n"
        + query
    )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text

        return answer

    except Exception as e:

        return (
            f"Error generating response: {str(e)}"
        )