from fastapi import (
    FastAPI,
    UploadFile,
    File
)

import shutil
from fastapi.middleware.cors import CORSMiddleware

from backend.ingest import ingest_pdf
from backend.query_engine import ask_question

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "RAG Chatbot Ready"
    }


@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    save_path = (
        f"storage/uploads/{file.filename}"
    )

    with open(
        save_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunk_count = ingest_pdf(
        save_path
    )

    return {
        "status": "success",
        "chunks": chunk_count
    }


@app.post("/ask")
async def ask(
    payload: dict
):

    question = payload["question"]

    answer = ask_question(
        question
    )

    return {
        "answer": answer
    }