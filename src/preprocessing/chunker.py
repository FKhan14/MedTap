import re

def chunk_pubmed_text(text):
    sections = re.split(r'\n\d+\.', text)
    chunks = [s.strip() for s in sections if s.strip()]
    return chunks

if __name__ == "__main__":
    with open("data/raw/pubmed/hypertension symptoms treatment.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    chunks = chunk_pubmed_text(text)
    print(f"Number of chunks: {len(chunks)}")
    print(f"First chunk preview:\n{chunks[0][:300]}")