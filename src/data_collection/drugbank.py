import xml.etree.ElementTree as ET
import json
import os

NS = "{http://www.drugbank.ca}"
DRUGBANK_FILE = "data/raw/drugbank/full database.xml"

def parse_interactions(limit=100):
    print("Parsing DrugBank XML...")
    tree = ET.parse(DRUGBANK_FILE)
    root = tree.getroot()
    
    interactions = []
    
    for drug in root.findall(f"{NS}drug"):
        name = drug.findtext(f"{NS}name")
        
        drug_interactions = drug.find(f"{NS}drug-interactions")
        if drug_interactions is None:
            continue
            
        for interaction in drug_interactions.findall(f"{NS}drug-interaction"):
            interacting_drug = interaction.findtext(f"{NS}name")
            description = interaction.findtext(f"{NS}description")
            
            if name and interacting_drug and description:
                interactions.append({
                    "drug1": name,
                    "drug2": interacting_drug,
                    "interaction": description
                })
        
        if len(interactions) >= limit:
            break
    
    return interactions

def save_interactions(interactions):
    folder = "data/raw/drugbank"
    os.makedirs(folder, exist_ok=True)
    
    file_path = f"{folder}/interactions.json"
    with open(file_path, "w") as f:
        json.dump(interactions, f, indent=2)
    print(f"Saved {len(interactions)} interactions to {file_path}")
    
if __name__ == "__main__":
    interactions = parse_interactions(limit=50000)
    print(f"Found {len(interactions)} interactions")
    save_interactions(interactions)