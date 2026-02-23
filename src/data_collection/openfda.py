import requests
import json
import os

BASE_URL = "https://api.fda.gov/drug/label.json"
FIELDS_TO_KEEP = ["indications_and_usage","warnings","dosage_and_administration","active_ingredient","purpose","do_not_use","ask_doctor"]
DRUG_LIST = ["ibuprofen","acetaminophen","naproxen","amoxicillin","azithromycin","ciprofloxacin","lisinopril","amlodipine","metoprolol","metformin","glipizide","sertraline","fluoxetine","cetirizine","albuterol","omeprazole","pantoprazole","simvastatin","atorvastatin","rosuvastatin","hydrochlorothiazide", "losartan", "gabapentin", "levothyroxine",
"prednisone", "tramadol", "cyclobenzaprine", "meloxicam",
"doxycycline", "cephalexin", "trimethoprim", "clindamycin",
"ranitidine", "loratadine", "montelukast", "insulin",
"warfarin", "clopidogrel", "atenolol", "furosemide", "spironolactone", "sildenafil", "tadalafil", "lansoprazole", "rabeprazole", "esomeprazole", "dexlansoprazole","fluconazole", "ketoconazole", "miconazole", "nystatin"]
def fetch_drug_label(drug_name, limit =10):
    params = {"search": f"openfda.brand_name:{drug_name}", "limit": limit}
    try:
        response = requests.get(BASE_URL,params = params)
        return response.json()
    except Exception as e:
        print(f"Error fetching data from OpenFDA: {e}")
        return None

def extract_fields(drug_result):
    return {field: drug_result.get(field) for field in FIELDS_TO_KEEP}

def save_to_json(name,data):
    folder = f"data/raw/openfda"
    os.makedirs(folder, exist_ok=True)
    
    file_path = f"{folder}/{name}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
        
        
def collect_all_drugs():
    for drug in DRUG_LIST:
        print(f"Collecting data for {drug}...")
        result = fetch_drug_label(drug)
        if result and "results" in result:
            single_drug = result["results"][0]
            cleaned = extract_fields(single_drug)
            save_to_json(drug, cleaned)
            print(f"Data for {drug} saved successfully.")
        else:
            print(f"No data found for {drug}.")

if __name__ == "__main__":
    collect_all_drugs()