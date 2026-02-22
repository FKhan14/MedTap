import requests
import json
import os

BASE_URL = "https://api.fda.gov/drug/label.json"
FIELDS_TO_KEEP = ["indications_and_usage","warnings","dosage_and_administration","active_ingredient","purpose","do_not_use","ask_doctor"]

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

if __name__ == "__main__":
    result = fetch_drug_label("ibuprofen")
    single_drug = result["results"][0]
    cleaned = extract_fields(single_drug)
    print(json.dumps(cleaned, indent=2))