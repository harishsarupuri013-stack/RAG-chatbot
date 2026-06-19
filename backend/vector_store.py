from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "storage" / "chroma"

print("CHROMA PATH:", CHROMA_PATH)

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_or_create_collection(
    name="documents"
)