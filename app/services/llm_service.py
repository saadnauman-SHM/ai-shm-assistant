import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.core.logger import get_logger

logger = get_logger(__name__)

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Knowledge base (your SHM knowledge)
def load_documents():
    with open("data/shm_knowledge.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Split into chunks (by line)
    documents = [line.strip() for line in text.split("\n") if line.strip()]
    return documents


documents = load_documents()

# Create embeddings
embeddings = model.encode(documents)
embeddings = np.array(embeddings).astype('float32')

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def query(prompt: str):
    logger.info(f"Received prompt: {prompt}")

    if not prompt.strip():
        logger.error("Empty prompt")
        raise ValueError("Question cannot be empty")

    # Convert query to embedding
    query_vector = model.encode([prompt]).astype('float32')

    # Search top 2 results
    k = 2
    distances, indices = index.search(query_vector, k)

    results = [documents[i] for i in indices[0]]

    logger.info(f"Retrieved results: {results}")

    answer = f"""
    Based on available SHM knowledge:

    - {results[0]}
    - {results[1]}

    This suggests that structural health monitoring detects damage using sensors and structural analysis techniques.
    """

    return {
        "generated_text": answer.strip()
    }