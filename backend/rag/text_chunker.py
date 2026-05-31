from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):

    all_chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    for doc in documents:

        chunks = splitter.split_text(doc)

        all_chunks.extend(chunks)

    return all_chunks