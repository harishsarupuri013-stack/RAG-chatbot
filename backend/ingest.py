from backend.utils import extract_text
from backend.utils import create_chunks
from backend.vector_store import collection

def ingest_pdf(pdf_path):

    text = extract_text(pdf_path)

    chunks = create_chunks(text)

    if len(chunks) == 0:
        return 0

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        ids=ids,
        documents=chunks
    )

    return len(chunks)