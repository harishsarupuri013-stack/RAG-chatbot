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



def create_chunks(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks