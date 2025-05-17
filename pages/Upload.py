import streamlit as st

st.title("📤 Upload")
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    st.write("Uploaded:", uploaded_file.name)
