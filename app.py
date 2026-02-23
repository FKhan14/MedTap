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

# Header
st.markdown("""
    <h1 style='text-align: center; color: #2E86AB;'> MedTap</h1>
    <p style='text-align: center; color: #666; font-size: 18px;'>
    Medical Reference Assistant for Low-Income Clinics</p>
    <hr>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### About MedTap")
    st.write("MedTap is a free medical reference tool built for clinic workers at low-income clinics.")
    st.markdown("### Data Sources")
    st.write("• FDA Drug Labels")
    st.write("• PubMed Medical Literature")
    st.markdown("### Coverage")
    st.write("• 51 common drugs")
    st.write("• 10 medical conditions")
    st.warning("MedTap is a reference tool only. Always apply clinical judgment.")

# Main
query = st.text_input("", placeholder="Ask a medical question...")

col1, col2, col3 = st.columns([1,1,1])
with col2:
    search = st.button("Search", use_container_width=True)

if search and query:
    with st.spinner("Searching medical database..."):
        chunks = retrieve(query, top_k=10)
        response = generate_response(query, chunks)

    st.markdown("### MedTap Response")
    st.info(response)

    st.markdown("### Sources")
    for r in chunks[:3]:
        with st.expander(f" {r[1].title()} | {r[2].replace('_', ' ').title()} | Similarity: {r[4]:.3f}"):
            st.write(r[3])