EVAL_SET = [
    {
        "query": "What are the warnings for ibuprofen?",
        "expected_source": "ibuprofen",
        "expected_field": "warnings"
    },
    {
        "query": "What is metformin used for?",
        "expected_source": "metformin",
        "expected_field": "indications_and_usage"
    },
    {
        "query": "How do you dose amoxicillin?",
        "expected_source": "amoxicillin",
        "expected_field": "dosage_and_administration"
    },
    {
        "query": "What are contraindications for lisinopril?",
        "expected_source": "lisinopril",
        "expected_field": "do_not_use"
    },
    {
        "query": "What does sertraline treat?",
        "expected_source": "sertraline",
        "expected_field": "indications_and_usage"
    },
    {
        "query": "What are the side effects of azithromycin?",
        "expected_source": "azithromycin",
        "expected_field": "warnings"
    },
    {
        "query": "What is albuterol used for?",
        "expected_source": "albuterol",
        "expected_field": "indications_and_usage"
    },
    {
        "query": "How do you dose acetaminophen?",
        "expected_source": "acetaminophen",
        "expected_field": "dosage_and_administration"
    },
    {
        "query": "What should you not take with omeprazole?",
        "expected_source": "omeprazole",
        "expected_field": "do_not_use"
    },
    {
        "query": "What does fluoxetine treat?",
        "expected_source": "fluoxetine",
        "expected_field": "indications_and_usage"
    }
    
]

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from retrieval import retrieve

def evaluate(top_k=5):
    hits = 0
    for item in EVAL_SET:
        results = retrieve(item["query"], top_k=top_k)
        for r in results:
            if r[1] == item["expected_source"] and r[2] == item["expected_field"]:
                hits += 1
                break
    precision = hits / len(EVAL_SET)
    print(f"Precision@{top_k}: {precision:.2f} ({hits}/{len(EVAL_SET)})")
    return precision

if __name__ == "__main__":
    evaluate(top_k=5)
    evaluate(top_k=10)
    evaluate(top_k=15)