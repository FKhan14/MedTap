import re
import json

def chunk_pubmed_text(text):
    sections = re.split(r'\n\d+\.', text)
    chunks = [s.strip() for s in sections if s.strip()]
    return chunks

def chunk_openfda_data(data):
    chunks = []
    for field, value in data.items():
        if value:
            # value is a list, get the first item
            text = value[0] if isinstance(value, list) else value
            chunks.append(f"{field}: {text}")
    return chunks

def chunk_drugbank_interactions(interactions):
    chunks = []
    for item in interactions:
        text = f"drug_interaction: {item['drug1']} and {item['drug2']} - {item['interaction']}"
        chunks.append(text)
    return chunks

if __name__ == "__main__":
    with open("data/raw/openfda/ibuprofen.json", "r") as f:
        drug_data = json.load(f)

    drug_chunks = chunk_openfda_data(drug_data)
    print(f"Drug chunks: {len(drug_chunks)}")
    for chunk in drug_chunks:
        print(chunk[:100])