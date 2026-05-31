import pickle

from utils.pdf_loader import load_pdf

from rag.text_chunker import chunk_documents
from rag.embedder import embed_chunks
from rag.faiss_store import store_embeddings


def rebuild_from_pdf(file_path):

    print("Reading PDF...")

    text = load_pdf(file_path)

    documents = [text]

    print("Creating chunks...")

    chunks = chunk_documents(documents)

    with open(
        "data/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

    print(
        f"Saved {len(chunks)} chunks"
    )

    print(
        "Generating embeddings..."
    )

    embeddings = embed_chunks(
        chunks
    )

    print(
        "Updating FAISS..."
    )

    store_embeddings(
        embeddings
    )

    print(
        "FAISS updated successfully!"
    )

    return len(chunks)