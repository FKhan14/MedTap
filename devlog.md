# MedTap Devlog

## 2/20/2026 - Day 1

**What I'm building:**
I am building a tool designed to help low-income clinic workers 

**Why:**
I made this in honor of the woman who helped my mom with her cancer fight.

**What I did today:**
Today I set up the data strategy, user, build order, Full Stack, and scope, as
well as created the initial file structure and downloaded dependencies.

**What's next:**
- Verify Python, PostgreSQL, pip
- Start Phase 1: Data Collection


## 2/22/2026 - Day 2

**What I did today:**
Phase 1 - Data Collection:
- openFDA fetcher: pulls drug label data from the FDA API
- Field extraction: filters raw data to only the 7 fields MedTap needs
- Bulk drug collection: automatically collected 20 common drugs
- PubMed fetcher: two-step search then fetch for medical abstracts
- Bulk condition collection: collected 10 common conditions

Phase 2 - Preprocessing:
- PubMed chunker: splits multi-article text into individual article chunks
- openFDA chunker: splits drug JSON into field-based chunks with field 
  names included for better retrieval context

**What's next:**
- Phase 3: Embeddings and Database
- Convert chunks into vector embeddings using PubMedBERT
- Store embeddings in Supabase pgvector
