from sentence_transformers import SentenceTransformer

from transformers import T5Tokenizer
from transformers import T5ForConditionalGeneration


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