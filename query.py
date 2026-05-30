import pickle
import time

from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer

from transformers import T5Tokenizer
from transformers import T5ForConditionalGeneration


# =========================
# LOAD VECTOR STORE
# =========================

with open("vector_store.pkl", "rb") as file:

    data = pickle.load(file)


chunks = data["chunks"]

chunk_embeddings = data["embeddings"]


# =========================
# LOAD EMBEDDING MODEL
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# LOAD GENERATION MODEL
# =========================

tokenizer = T5Tokenizer.from_pretrained(
    "google/flan-t5-base"
)

generator_model = T5ForConditionalGeneration.from_pretrained(
    "google/flan-t5-base"
)


# =========================
# USER QUESTION
# =========================

question = input("Ask Question: ")


# =========================
# QUESTION EMBEDDING
# =========================

question_embedding = embedding_model.encode(question)


# =========================
# SIMILARITY SEARCH
# =========================

similarities = cosine_similarity(
    [question_embedding],
    chunk_embeddings
)


best_match_index = similarities.argmax()

best_chunk = chunks[best_match_index]


print("\nRetrieved Context:\n")

print(best_chunk)


# =========================
# PROMPT
# =========================

prompt = f"""
Answer the question using the context below.

Context:
{best_chunk}

Question:
{question}

Answer:
"""


# =========================
# GENERATION
# =========================

start_time = time.time()


inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True
)


outputs = generator_model.generate(
    **inputs,
    max_new_tokens=100
)


answer = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


end_time = time.time()

total_time = end_time - start_time


# =========================
# FINAL OUTPUT
# =========================

print("\nANSWER:\n")

print(answer)

print("\nGeneration Time:", total_time, "seconds")