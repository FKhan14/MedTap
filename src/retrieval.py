import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_connection
from preprocessing.embedder import embed_chunks

def retrieve(query, top_k=5):
    conn = get_connection()
    query_embedding = embed_chunks([query])[0].tolist()
    
    with conn.cursor() as cur:
        cur.execute("""
            SELECT source, source_name, field_type, content,
                   1 - (embedding <=> %s::vector) AS similarity
            FROM medical_chunks
            ORDER BY similarity DESC
            LIMIT %s
        """, (str(query_embedding), top_k))
        
        results = cur.fetchall()
    
    return results

if __name__ == "__main__":
    results = retrieve("what are the side effects of ibuprofen?")
    for r in results:
        print(f"Source: {r[1]} | Field: {r[2]} | Similarity: {r[4]:.3f}")
        print(f"Content: {r[3][:150]}")
        print("---")