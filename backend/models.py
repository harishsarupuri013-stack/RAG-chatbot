from sentence_transformers import SentenceTransformer

from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration
)

embedding_model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

tokenizer = T5Tokenizer.from_pretrained(
    "google/flan-t5-base"
)

generator_model = T5ForConditionalGeneration.from_pretrained(
    "google/flan-t5-base"
)