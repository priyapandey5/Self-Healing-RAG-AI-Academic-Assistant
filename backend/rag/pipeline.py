import pickle

from utils.file_loader import document_loader
from rag.text_chunker import chunk_documents
from rag.embedder import embed_chunks
from rag.faiss_store import store_embeddings


def run_pipeline():

    print("Loading documents...")
    documents = document_loader()
    print(f"Loaded {len(documents)} documents")

    print("Creating chunks...")
    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")

    # Save chunks
    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Chunks saved successfully!")

    print("Generating embeddings...")
    embeddings = embed_chunks(chunks)

    print("Storing embeddings in FAISS...")
    store_embeddings(embeddings)

    print("FAISS index created successfully!")

    return chunks


if __name__ == "__main__":
    run_pipeline()