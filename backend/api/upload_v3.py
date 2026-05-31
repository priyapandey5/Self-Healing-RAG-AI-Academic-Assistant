from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from rag.rebuild_index import rebuild_from_pdf

import os

from rag.rebuild_index import rebuild_from_pdf

router = APIRouter()

UPLOAD_FOLDER = "data/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    if not (
        file.filename.endswith(".pdf")
        or
        file.filename.endswith(".txt")
    ):
        return {
            "error": "Only PDF and TXT files allowed"
        }

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()
        f.write(content)

    # -------------------------
    # REBUILD VECTOR DATABASE
    # -------------------------

    chunk_count = rebuild_from_pdf(
        file_path
    )

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "chunks_created": chunk_count
    }