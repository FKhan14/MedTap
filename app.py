import streamlit as st
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from retrieval import retrieve
from llm import generate_response

st.set_page_config(
    page_title="MedTap",
    page_icon="🏥",
    layout="wide"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown("""
    <h1 style='text-align: center; color: #2E86AB;'>🏥 MedTap</h1>
    <p style='text-align: center; color: #666; font-size: 18px;'>
    Medical Reference Assistant for Low-Income Clinics</p>
    <hr>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### About MedTap")
    st.write("A free medical reference tool for clinic workers.")
    st.markdown("### Coverage")
    st.write("• 51 common drugs")
    st.write("• 10 medical conditions")
    st.warning("Reference tool only. Always apply clinical judgment.")
    
    if st.session_state.chat_history:
        st.markdown("### 📜 Session History")
        for item in reversed(st.session_state.chat_history):
            with st.expander(f"Q: {item['question'][:40]}..."):
                st.write(item["answer"])
        if st.button("Clear History"):
            st.session_state.chat_history = []

tab1, tab2 = st.tabs(["💊 Drug Lookup", "🔍 Symptom Checker"])

with tab1:
    st.markdown("### Drug Lookup")
    st.write("Enter a drug name to get structured information.")
    
    drug_query = st.text_input("Drug name:", 
                                placeholder="e.g. ibuprofen, metformin")
    
    info_type = st.selectbox("What do you need to know?", [
        "General Overview",
        "Warnings",
        "Dosage",
        "Contraindications",
        "Active Ingredients"
    ])
    
    type_map = {
        "General Overview": "what is",
        "Warnings": "warnings and side effects",
        "Dosage": "dosage and administration",
        "Contraindications": "do not use contraindications",
        "Active Ingredients": "active ingredients"
    }
    
    if st.button("🔍 Look Up Drug", use_container_width=True) and drug_query:
        query = f"{type_map[info_type]} for {drug_query}"
        with st.spinner(f"Looking up {drug_query}..."):
            chunks = retrieve(query, top_k=10)
            response = generate_response(query, chunks)
        
        st.session_state.chat_history.append({
            "question": query,
            "answer": response
        })
        
        st.markdown(f"### {drug_query.title()} — {info_type}")
        st.info(response)
        
        st.markdown("### Sources")
        for r in chunks[:3]:
            with st.expander(f"📄 {r[1].title()} | {r[2].replace('_',' ').title()} | Similarity: {r[4]:.3f}"):
                st.write(r[3])

with tab2:
    st.markdown("### Symptom Checker")
    st.write("Enter patient symptoms to get possible conditions and treatments.")
    
    symptoms = st.text_area("Patient symptoms:", 
                             placeholder="e.g. fever, sore throat, difficulty swallowing")
    
    if st.button("🔍 Check Symptoms", use_container_width=True) and symptoms:
        query = f"patient symptoms {symptoms} possible conditions treatment"
        with st.spinner("Analyzing symptoms..."):
            chunks = retrieve(query, top_k=10)
            response = generate_response(query, chunks)
        
        st.session_state.chat_history.append({
            "question": query,
            "answer": response
        })
        
        st.markdown("### Possible Conditions and Treatments")
        st.info(response)
        
        st.markdown("### Sources")
        for r in chunks[:3]:
            with st.expander(f"📄 {r[1].title()} | {r[2].replace('_',' ').title()} | Similarity: {r[4]:.3f}"):
                st.write(r[3])