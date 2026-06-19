import faiss
import pickle
import numpy as np
from backend.vector_store import collection

from backend.models import (
    tokenizer,
    generator_model
)


def ask_question(question):

    results = collection.query(
        query_texts=[question],
        n_results=5
    )

    retrieved_chunks = results["documents"][0]
    print(retrieved_chunks)

    context = "\n\n".join(retrieved_chunks)

    return retrieved_chunks[0]
    # prompt = f"""
    # Answer only from the context.

    # Context:
    # {context}

    # Question:
    # {question}

    # Answer:
    # """

    # inputs = tokenizer(
    #     prompt,
    #     return_tensors="pt",
    #     truncation=True
    # )

    # outputs = generator_model.generate(
    #     **inputs,
    #     max_new_tokens=150
    # )

    # answer = tokenizer.decode(
    #     outputs[0],
    #     skip_special_tokens=True
    # )

    # return answer