import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from retrieval import retrieve
from llm import generate_response

def ask_medtap(query):
    print(f"\nSearching for: {query}")
    chunks = retrieve(query, top_k=5)
    print(f"Found {len(chunks)} relevant chunks")
    
    response = generate_response(query, chunks)
    return response

if __name__ == "__main__":
    while True:
        query = input("\nClinic Worker Question (or 'quit'): ")
        if query.lower() == "quit":
            break
        answer = ask_medtap(query)
        print(f"\nMedTap: {answer}")