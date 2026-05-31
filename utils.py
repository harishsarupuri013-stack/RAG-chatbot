import fitz


def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    all_text = ""

    for page_number in range(len(document)):

        page = document[page_number]

        text = page.get_text()

        if text:

            cleaned_text = text.replace("\n", " ")

            all_text += cleaned_text + " "

    return all_text



def create_chunks(text, chunk_size=200, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks