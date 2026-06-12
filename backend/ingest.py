import faiss
import pickle
import numpy as np

from backend.models import embedding_model
from backend.utils import extract_text
from backend.utils import create_chunks


def ingest_pdf(pdf_path):

    text = extract_text(pdf_path)

    chunks = create_chunks(text)

    embeddings = embedding_model.encode(
        chunks
    )

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    faiss.write_index(
        index,
        "storage/vector.index"
    )

    with open(
        "storage/chunks.pkl",
        "wb"
    ) as file:

        pickle.dump(
            chunks,
            file
        )

    return len(chunks)