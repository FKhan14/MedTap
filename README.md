# MedTap

A medical reference RAG system built for low-income clinics.

## Why I Built This
I built this from my own experiences in low-income clinics, noticing how they lack tools to help them in their work.

## What It Does
- Symptom and condition lookup using PubMed medical literature
- Drug information including dosage, warnings, and contraindications
- Semantic search that understands meaning, not just keywords

## Tech Stack
- PubMedBERT for domain-specific medical embeddings
- pgvector + Supabase for vector similarity search
- Llama 3.2 via Ollama for free local LLM inference
- openFDA and PubMed APIs for medical data

## Performance
- Precision@5: 0.70 on held-out QA evaluation set
- 20 drugs and 10 conditions indexed

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Install Ollama and pull Llama 3.2: `ollama pull llama3.2`
4. Add your Supabase credentials to `.env`
5. Run: `streamlit run app.py`

## Data Sources
- openFDA API - drug labels and contraindications
- PubMed API - medical literature abstracts
