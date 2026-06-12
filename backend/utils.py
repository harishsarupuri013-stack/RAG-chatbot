import fitz


def extract_text(pdf_path):

    document = fitz.open(pdf_path)

    text = ""

    for page in document:

        text += page.get_text()

    return text


def create_chunks(
    text,
    chunk_size=1000,
    overlap=200
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks