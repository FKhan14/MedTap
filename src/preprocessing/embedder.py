from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb"
model = SentenceTransformer(MODEL_NAME)

def embed_chunks(chunks):
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    test_chunks = [
        "warnings: Ibuprofen may cause severe allergic reactions",
        "indications_and_usage: temporarily relieves minor aches and pains"
    ]
    embeddings = embed_chunks(test_chunks)
    print(f"Number of embeddings: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")