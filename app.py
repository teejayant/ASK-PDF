
import streamlit as st
from pdf_reader import extract_text_from_pdf
from gemini_qa import get_gemini_response, summarize_answer, get_pdf_summary

# Streamlit page setup
st.set_page_config(page_title="PDF QA with Gemini", layout="centered")
st.title("📄 ASK PDF")

# # Precaution message for PDF size limit
# st.info("⚠️ Please upload PDF files having less than 300 pages  to avoid memory errors and API quota issues.")

# Upload PDF
pdf_file = st.file_uploader("📁 Upload your PDF", type="pdf")

# Initialize session state variables
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "text" not in st.session_state:
    st.session_state.text = ""

if pdf_file:
    text = extract_text_from_pdf(pdf_file)
    st.session_state.text = text

    st.success("✅ PDF uploaded and processed!")

    # Summary Button
    if st.button("🧠 Summarize PDF"):
        with st.spinner("Summarizing PDF..."):
            st.session_state.summary = get_pdf_summary(text)

    # Show summary if already generated
    if st.session_state.summary:
        st.subheader("📌 Summary:")
        st.write(st.session_state.summary)

    # Question Input & Answer
    question = st.text_input("💬 Ask a Question")

    if st.button("Get Answer") and question:
        with st.spinner("Answering your question..."):
            answer = get_gemini_response(st.session_state.text, question)
            answer_summary = summarize_answer(answer)

            st.subheader("📝 Answer:")
            st.write(answer)

            st.subheader("📌 Summary of Answer:")
            st.write(answer_summary)




#how to run app:
#python--version
#.\venv_311\Scripts\activate --> activate virtual environment
#  Run the command in terminal --> streamlit run app.py
# This will start a local server and open the app in your default web browser.

# Example questions you can ask:
# Which income source had the highest variance from the budget?
# What was the largest actual expense category?”
# “List all expense categories where actual exceeded budget.”
# “Which category was most under budget?”
# “How much was spent on personnel expenses?”
#“I understood Laevsky from the very first month of our acquaintance,”
#‘Courage, friends, and do not yield!’ on which page no of this pdf are these lines spoken?

