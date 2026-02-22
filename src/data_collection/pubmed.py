import requests
import json
import os
SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

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

if __name__ == "__main__":
    ids = search_pubmed("ibuprofen")
    abstracts = fetch_pubmed_details(ids)
    print(abstracts[:500])