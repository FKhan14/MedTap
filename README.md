# MedTap

### A Free, Open-Source Medical Reference System for Low-Income Clinics

**MedTap** is a lightweight, zero-cost clinical reference tool built for healthcare workers serving under-resourced communities.

Named after **Mehtep** — a woman who helped a family through cancer — this project is dedicated to clinics that care for patients who can’t afford anything else.

---

## Mission

Provide fast, reliable, evidence-grounded medical reference information — completely free — for frontline healthcare providers in low-income settings.

---

##  Features

###  Drug Lookup

* Dosage information
* Warnings
* Contraindications
* Clinical notes
* 51 commonly prescribed medications indexed

###  Symptom Checker

* Suggests possible conditions
* Grounded in real medical literature
* Retrieval-Augmented Generation (RAG) pipeline

###  Drug Interaction Checker

* Check interaction risks between two medications

###  Session History

* Tracks all queries during a shift
* Allows quick reference to previous lookups

---

## System Architecture

```
openFDA + PubMed APIs
        ↓
PubMedBERT Embeddings
        ↓
pgvector + Supabase
        ↓
Llama 3.2 (local, free via Ollama)
        ↓
Streamlit Interface
```

### Stack Overview

* **Data Sources:** openFDA, PubMed
* **Embeddings:** PubMedBERT
* **Vector Database:** pgvector (Supabase)
* **LLM:** Llama 3.2 (local via Ollama)
* **Frontend:** Streamlit

---

##  Performance

* **Precision@15:** 0.70 on held-out QA evaluation set
* **51 drugs**, **10 conditions** indexed
* **Zero inference cost** (runs fully local)

---

##  Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/medtap.git
cd medtap
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Pull the LLM

```
ollama pull llama3.2
```

### 4. Run the app

```
streamlit run app.py
```

---

##  Roadmap (V2)

* DrugBank integration
* Pediatric dosing support
* Spanish language support
* Pilot deployment in a free clinic in Boston

---

##  Disclaimer

MedTap is intended as a **clinical reference support tool** and does not replace professional medical judgment, diagnosis, or treatment decisions.

---

##  Why This Exists

Healthcare workers in low-income clinics often lack access to expensive reference systems like UpToDate. MedTap exists to close that gap — with open tools, open data, and zero cost.
