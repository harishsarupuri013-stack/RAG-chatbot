import pickle

from sentence_transformers import SentenceTransformer

from utils import extract_text_from_pdf
from utils import create_chunks


# =========================
# LOAD EMBEDDING MODEL
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# EXTRACT PDF TEXT
# =========================

pdf_path = "pranav_fusion.pdf"

text = extract_text_from_pdf(pdf_path)


# =========================
# CREATE CHUNKS
# =========================

chunks = create_chunks(text)


print("Total Chunks:", len(chunks))


# =========================
# CREATE EMBEDDINGS
# =========================

chunk_embeddings = embedding_model.encode(chunks)


# =========================
# STORE DATA
# =========================

data = {
    "chunks": chunks,
    "embeddings": chunk_embeddings
}


# =========================
# SAVE TO DISK
# =========================

with open("vector_store.pkl", "wb") as file:

    pickle.dump(data, file)


print("Embeddings stored successfully!")