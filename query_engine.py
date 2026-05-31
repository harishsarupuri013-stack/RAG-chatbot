import pickle
import faiss
import numpy as np

from models import embedding_model
from models import tokenizer
from models import generator_model


# =========================
# LOAD VECTOR INDEX
# =========================

index = faiss.read_index("vector.index")


# =========================
# LOAD CHUNKS
# =========================

with open("chunks.pkl", "rb") as file:

    chunks = pickle.load(file)



def ask_question(question):

    # =========================
    # QUESTION EMBEDDING
    # =========================

    question_embedding = embedding_model.encode([question])

    question_embedding = np.array(
        question_embedding,
        dtype="float32"
    )


    # =========================
    # TOP-K RETRIEVAL
    # =========================

    top_k = 3

    distances, indices = index.search(
        question_embedding,
        top_k
    )


    # =========================
    # BUILD CONTEXT
    # =========================

    retrieved_chunks = []

    for idx in indices[0]:

        retrieved_chunks.append(chunks[idx])


    context = "\n\n".join(retrieved_chunks)


    # =========================
    # PROMPT
    # =========================

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If answer is not present in the context, say:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""


    # =========================
    # TOKENIZATION
    # =========================

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )


    # =========================
    # GENERATION
    # =========================

    outputs = generator_model.generate(
        **inputs,
        max_new_tokens=100
    )


    # =========================
    # DECODE
    # =========================

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


    return answer