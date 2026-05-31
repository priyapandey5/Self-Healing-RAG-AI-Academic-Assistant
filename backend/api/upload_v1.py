from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

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

    return {
        "message": "File uploaded",
        "filename": file.filename
    }