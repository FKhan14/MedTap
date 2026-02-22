import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import get_connection
from preprocessing.chunker import chunk_openfda_data, chunk_pubmed_text
from preprocessing.embedder import embed_chunks

def store_chunk(conn, source, source_name, field_type, content, embedding):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO medical_chunks 
            (source, source_name, field_type, content, embedding)
            VALUES (%s, %s, %s, %s, %s)
        """, (source, source_name, field_type, content, embedding.tolist()))
        conn.commit()
        
def process_all_data():
    conn = get_connection()
    
    # Process openFDA drugs
    for filename in os.listdir("data/raw/openfda"):
        if filename.endswith(".json"):
            drug_name = filename.replace(".json", "")
            print(f"Processing {drug_name}...")
            
            with open(f"data/raw/openfda/{filename}", "r") as f:
                data = json.load(f)
            
            chunks = chunk_openfda_data(data)
            embeddings = embed_chunks(chunks)
            
            for chunk, embedding in zip(chunks, embeddings):
                store_chunk(conn, "openfda", drug_name, 
                          chunk.split(":")[0], chunk, embedding)
    
    # Process PubMed conditions
    for filename in os.listdir("data/raw/pubmed"):
        if filename.endswith(".txt"):
            condition_name = filename.replace(".txt", "")
            print(f"Processing {condition_name}...")
            
            with open(f"data/raw/pubmed/{filename}", "r", 
                      encoding="utf-8", errors="ignore") as f:
                text = f.read()
            
            chunks = chunk_pubmed_text(text)
            embeddings = embed_chunks(chunks)
            
            for chunk, embedding in zip(chunks, embeddings):
                store_chunk(conn, "pubmed", condition_name, 
                           "abstract", chunk, embedding)

if __name__ == "__main__":
    process_all_data()