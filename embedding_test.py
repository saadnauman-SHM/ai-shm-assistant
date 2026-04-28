from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model (downloads first time)
model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [
    "Bridge crack detection",
    "Structural damage monitoring",
    "Cooking pasta recipe"
]

# Generate embeddings
embeddings = model.encode(texts)

# Compare similarity
similarity = cosine_similarity([embeddings[0]], embeddings)

print("Similarity scores:")
for i, score in enumerate(similarity[0]):
    print(f"{texts[i]} → {score:.2f}")