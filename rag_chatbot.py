from transformers import T5Tokenizer, T5ForConditionalGeneration
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import fitz
import time


# =========================
# EMBEDDING MODEL
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# GENERATION MODEL
# =========================

tokenizer = T5Tokenizer.from_pretrained(
    "google/flan-t5-base"
)

generator_model = T5ForConditionalGeneration.from_pretrained(
    "google/flan-t5-base"
)


# =========================
# LOAD PDF
# =========================

pdf_path = "pranav_fusion.pdf"

document = fitz.open(pdf_path)

all_text = ""


# =========================
# EXTRACT TEXT
# =========================

for page_number in range(len(document)):

    page = document[page_number]

    text = page.get_text()

    if text:

        cleaned_text = text.replace("\n", " ")

        all_text += cleaned_text + " "


# =========================
# CHUNKING
# =========================

chunk_size = 500

chunks = []

for i in range(0, len(all_text), chunk_size):

    chunk = all_text[i:i + chunk_size]

    chunks.append(chunk)


print("Total Chunks:", len(chunks))


# =========================
# CREATE EMBEDDINGS
# =========================

chunk_embeddings = embedding_model.encode(chunks)


# =========================
# USER QUESTION
# =========================

question = "What are supported file formats?"


# =========================
# QUESTION EMBEDDING
# =========================

question_embedding = embedding_model.encode(question)


# =========================
# COSINE SIMILARITY
# =========================

similarities = cosine_similarity(
    [question_embedding],
    chunk_embeddings
)


# =========================
# BEST MATCH
# =========================

best_match_index = similarities.argmax()

best_chunk = chunks[best_match_index]


print("\nBest Match Index:", best_match_index)

print("\nMOST RELEVANT CHUNK:\n")

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
# GENERATION START
# =========================

start_time = time.time()


# =========================
# TOKENIZATION
# =========================

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True
)


# =========================
# GENERATE ANSWER
# =========================

outputs = generator_model.generate(
    **inputs,
    max_new_tokens=100
)


# =========================
# DECODE OUTPUT
# =========================

answer = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


# =========================
# GENERATION END
# =========================

end_time = time.time()

total_time = end_time - start_time


# =========================
# FINAL OUTPUT
# =========================

print("\nANSWER:\n")

print(answer)

print("\nGeneration Time:", total_time, "seconds")