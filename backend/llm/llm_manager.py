from llm.gemini_client import client
from core.prompts import system_prompt
from rag.retriever import retrieve_chunks

def llm_response(query, conversation=None):

 similar_chunks = retrieve_chunks(query)

 context = "\n".join(
    chunk["text"]
    for chunk in similar_chunks
 )
 print("\n===== RETRIEVED CONTEXT =====")
 print(context)
 print("============================\n")
 sources = list(
    set(
        chunk["source"]
        for chunk in similar_chunks
    )
 )

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

    answer += "\n\n📄 Sources:\n"

    for source in sources:
        answer += f"\n• {source}"

    return answer

 except Exception as e:
    return f"Error generating response: {str(e)}"