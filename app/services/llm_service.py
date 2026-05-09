import os
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from openai import OpenAI

from app.core.logger import get_logger
from app.core.config import settings
from app.services.pdf_loader import extract_text_from_pdf

logger = get_logger(__name__)

# =========================
# Load embedding model
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================
# Load documents from PDFs
# =========================
def load_documents():
    documents = []

    pdf_folder = "data/pdfs"

    # Check if folder exists
    if not os.path.exists(pdf_folder):
        logger.error(f"PDF folder not found: {pdf_folder}")
        return []

    # Read all PDFs
    for filename in os.listdir(pdf_folder):

        if filename.endswith(".pdf"):

            pdf_path = os.path.join(pdf_folder, filename)

            logger.info(f"Loading PDF: {pdf_path}")

            text = extract_text_from_pdf(pdf_path)

            if not text:
                logger.warning(f"No text extracted from {filename}")
                continue

            # Split text into chunks
            chunks = text.split("\n\n")

            cleaned_chunks = [
                chunk.strip()
                for chunk in chunks
                if len(chunk.strip()) > 50
            ]

            documents.extend(cleaned_chunks)

    logger.info(f"Loaded {len(documents)} chunks from PDFs")

    return documents


# =========================
# Load knowledge base
# =========================
documents = load_documents()

if not documents:
    raise RuntimeError(
        "No documents loaded. Check your PDFs in data/pdfs"
    )


# =========================
# Create embeddings
# =========================
logger.info("Creating embeddings...")

embeddings = model.encode(
    documents,
    normalize_embeddings=True
)

embeddings = np.array(embeddings).astype("float32")


# =========================
# Build FAISS index
# =========================
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

logger.info("FAISS index ready")


# =========================
# Main query function
# =========================
def query(prompt: str):

    logger.info(f"Received prompt: {prompt}")

    if not prompt.strip():
        raise ValueError("Question cannot be empty")

    # =========================
    # Convert query to embedding
    # =========================
    query_vector = model.encode(
        [prompt],
        normalize_embeddings=True
    ).astype("float32")

    # =========================
    # Search FAISS
    # =========================
    k = min(3, len(documents))

    distances, indices = index.search(query_vector, k)

    results = [documents[i] for i in indices[0]]

    context = "\n".join(results)

    logger.info(f"Retrieved context: {context}")

    # =========================
    # Try real LLM
    # =========================
    try:

        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set")

        client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
You are an expert in Structural Health Monitoring (SHM).

Use the context below to answer the question clearly and professionally.

Context:
{context}

Question:
{prompt}

Answer:
"""
        )

        answer = response.output_text

        return {
            "generated_text": answer,
            "source": "real_llm"
        }

    # =========================
    # Fallback system
    # =========================
    except Exception as e:

        logger.warning(
            f"LLM failed, using fallback: {e}"
        )

        fallback = (
            "Based on retrieved SHM research knowledge:\n\n"
        )

        for r in results:
            fallback += f"- {r}\n"

        fallback += (
            "\nThis answer was generated using "
            "retrieval-based fallback."
        )

        return {
            "generated_text": fallback.strip(),
            "source": "faiss_fallback"
        }