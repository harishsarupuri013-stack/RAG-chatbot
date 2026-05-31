import pickle
import faiss
import numpy as np

from utils import extract_text_from_pdf
from utils import create_chunks

from models import embedding_model


# =========================
# LOAD PDF
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

chunk_embeddings = np.array(
    chunk_embeddings,
    dtype="float32"
)


# =========================
# CREATE FAISS INDEX
# =========================

dimension = chunk_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(chunk_embeddings)


# =========================
# SAVE INDEX
# =========================

faiss.write_index(index, "vector.index")


# =========================
# SAVE CHUNKS
# =========================

with open("chunks.pkl", "wb") as file:

    pickle.dump(chunks, file)


print("FAISS index created successfully!")