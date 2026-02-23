import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def generate_response(query, retrieved_chunks):
    context = "\n\n---\n\n".join([
        f"Source: {r[1]} | Type: {r[2]}\n{r[3]}"
        for r in retrieved_chunks
    ])
    
    prompt = f"""You are a medical reference assistant for healthcare professionals at low-income clinics.

RULES:
1. Answer ONLY using the provided context
2. If context is insufficient, say "I cannot find sufficient information"
3. Always cite your source
4. Never make definitive diagnoses
5. Always recommend clinical judgment

CONTEXT:
{context}

QUESTION: {query}

ANSWER:"""

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    
    return response.json()["response"]

if __name__ == "__main__":
    test_chunks = [
        ("openfda", "ibuprofen", "warnings", 
         "warnings: Ibuprofen may cause severe allergic reactions", 0.9),
        ("openfda", "ibuprofen", "dosage_and_administration",
         "dosage: take 1 tablet every 4-6 hours", 0.8)
    ]
    
    response = generate_response(
        "What are the warnings for ibuprofen?", 
        test_chunks
    )
    print(response)