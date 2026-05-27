import fitz

pdf_path = "sample.pdf"

document = fitz.open(pdf_path)

all_text = ""

for page_number in range(len(document)):
    page = document[page_number]
    text = page.get_text()
    cleaned_text = text.replace("\n", " ")
    all_text += text


chunk_size = 500

chunks = []

for i in range(0, len(all_text), chunk_size):

    chunk = all_text[i:i + chunk_size]

    chunks.append(chunk)

print("Total Chunks:", len(chunks))

print("\nFIRST CHUNK:\n")

print(chunks[0])