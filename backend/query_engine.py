import faiss
import pickle
import numpy as np

from backend.models import (
    embedding_model,
    tokenizer,
    generator_model
)


def ask_question(question):

    index = faiss.read_index(
        "storage/vector.index"
    )

    with open(
        "storage/chunks.pkl",
        "rb"
    ) as file:

        chunks = pickle.load(file)

    question_embedding = embedding_model.encode(
        [question]
    )

    question_embedding = np.array(
        question_embedding,
        dtype="float32"
    )

    top_k = 5

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    retrieved_chunks = []

    for idx in indices[0]:

        retrieved_chunks.append(
            chunks[idx]
        )

    context = "\n\n".join(
        retrieved_chunks
    )

    prompt = f"""
Answer only from the context.

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = generator_model.generate(
        **inputs,
        max_new_tokens=150
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer