import os
import pickle

from utils.pdf_loader import load_pdf

from rag.text_chunker import chunk_documents
from rag.embedder import embed_chunks
from rag.faiss_store import store_embeddings

UPLOAD_FOLDER = "data/uploads"

all_chunks = []

print("Reading PDFs...")

for filename in os.listdir(UPLOAD_FOLDER):

 if filename.endswith(".pdf"):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    print(f"Loading {filename}")

    text = load_pdf(file_path)

    chunks = chunk_documents([text])

    for chunk in chunks:

        all_chunks.append(
            {
                "text": chunk,
                "source": filename
            }
        )

print("Saving chunks...")

with open(
"data/chunks.pkl",
"wb"
) as f:

 pickle.dump(
    all_chunks,
    f
 )

print(
f"Saved {len(all_chunks)} chunks"
)

print(
"Generating embeddings..."
)

embeddings = embed_chunks(
[chunk["text"] for chunk in all_chunks]
)

print(
"Building FAISS index..."
)

store_embeddings(
embeddings
)

print(
"Knowledge Base Ready!"
)