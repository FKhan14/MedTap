import json

DRUG_LIST = ["ibuprofen","acetaminophen","naproxen","amoxicillin",
             "azithromycin","ciprofloxacin","lisinopril","amlodipine",
             "metoprolol","metformin","sertraline","fluoxetine",
             "warfarin","metoprolol","atorvastatin","gabapentin"]

with open("data/raw/drugbank/interactions.json", "r") as f:
    interactions = json.load(f)

relevant = [i for i in interactions 
            if i["drug1"].lower() in DRUG_LIST 
            or i["drug2"].lower() in DRUG_LIST]

print(f"Relevant interactions: {len(relevant)}")

with open("data/raw/drugbank/interactions_filtered.json", "w") as f:
    json.dump(relevant, f, indent=2)