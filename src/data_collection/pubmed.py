import requests
import json
import os
import time

SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CONDITION_LIST = [
    "hypertension symptoms treatment",
    "type 2 diabetes symptoms treatment",
    "upper respiratory infection symptoms",
    "urinary tract infection symptoms treatment",
    "asthma symptoms treatment",
    "depression symptoms treatment",
    "anxiety symptoms treatment",
    "gastroesophageal reflux symptoms treatment",
    "strep throat symptoms treatment",
    "pneumonia symptoms treatment"
]

def search_pubmed(query,max_results = 10):
    params = {"db":"pubmed",
              "term": query,
              "retmax": max_results,
              "retmode":"json"
              }
    try:
        response = requests.get(SEARCH_URL,params=params)
        return response.json()["esearchresult"]["idlist"]    
    except Exception as e:
        print(f"Error searching PubMed: {e}")
        return None
    
def fetch_pubmed_details(id_list):
    params = {"db":"pubmed",
              "id": ",".join(id_list),
              "rettype":"abstract",
              "retmode":"text"
              }
    try:
        response = requests.get(FETCH_URL,params=params)
        return response.text
    except Exception as e:
        print(f"Error fetching PubMed details: {e}")
        return None
def save_abstracts(query,text):
    folder = "data/raw/pubmed"
    os.makedirs(folder,exist_ok=True)
    file_path = f"{folder}/{query}.txt"
    with open(file_path, "w", encoding="utf-8",errors="ignore") as f:
        f.write(text)

def collect_all_conditions():
    for condition in CONDITION_LIST:
        print(f"Collecting data for {condition}...")
        ids = search_pubmed(condition)
        if ids:
            abstracts = fetch_pubmed_details(ids)
            save_abstracts(condition, abstracts)
            print(f"Saved {condition}")
        else:
            print(f"No results for {condition}")
        time.sleep(1)  

if __name__ == "__main__":
    collect_all_conditions()
    print("Saved Successfully")