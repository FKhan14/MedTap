import streamlit as st
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from retrieval import retrieve
from llm import generate_response

st.set_page_config(
    page_title="MedTap",
    layout="wide"
)

st.title("MedTap")
st.subheader("Medical Reference Assistant for Low-Income Clinics")
st.markdown("---")

query = st.text_input("Ask a medical question:", 
                       placeholder="e.g. What are the warnings for ibuprofen?")

if st.button("Search") and query:
    with st.spinner("Searching medical database..."):
        chunks = retrieve(query, top_k=10)
        response = generate_response(query, chunks)
    
    st.markdown("### MedTap Response")
    st.write(response)
    
    st.markdown("### Sources Retrieved")
    for r in chunks[:3]:
        with st.expander(f"{r[1]} | {r[2]} | Similarity: {r[4]:.3f}"):
            st.write(r[3])