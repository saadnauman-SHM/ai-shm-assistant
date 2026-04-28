import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Knowledge base (your SHM data)
documents = [
    "SHM monitors bridges for structural damage",
    "Sensors like accelerometers measure vibrations",
    "Cracks in structures can indicate failure",
    "Temperature changes affect structural integrity"
]

# Convert to embeddings
embeddings = model.encode(documents)

# Convert to numpy array
embeddings = np.array(embeddings).astype('float32')

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Query
query = "How do we detect damage in bridges?"
query_vector = model.encode([query]).astype('float32')

# Search
k = 2
distances, indices = index.search(query_vector, k)

print("Query:", query)
print("\nTop results:")
for i in indices[0]:
    print("-", documents[i])