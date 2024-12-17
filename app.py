import os
import fitz  # PyMuPDF for PDF text extraction
import google.generativeai as genai
import streamlit as st
import re

# Configuration for Gemini API
GEMINI_API_KEY = ""  #use your own API
genai.configure(api_key=GEMINI_API_KEY)

# Step 1: Extract text from PDF, including page info
def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file along with page numbers."""
    extracted_text = {}
    with fitz.open("pdf", pdf_file.read()) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            extracted_text[page_num + 1] = page.get_text()
    return extracted_text

# Step 2: Chunk text based on pages
def chunk_text_by_page(text_by_page, chunk_size=500, overlap=50):
    """Split text into chunks per page for easier querying."""
    chunked_data = {}
    for page_num, text in text_by_page.items():
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap
        chunked_data[page_num] = chunks
    return chunked_data

# Step 3: Query Gemini LLM
def query_gemini_llm(prompt):
    """Query the Gemini LLM and return the response."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Step 4: Extract specific data based on the user query
def extract_unemployment_info(chunks, query):
    """Search for specific unemployment data in the chunks."""
    relevant_chunks = []
    for page_num, chunks_list in chunks.items():
        for chunk in chunks_list:
            if "unemployment" in chunk.lower():  # Search for 'unemployment' keyword in the chunk
                relevant_chunks.append((page_num, chunk))

    # If relevant chunks found, use them for generating a more specific response
    if relevant_chunks:
        prompt = f"Here are the relevant chunks from the document regarding unemployment:\n"
        for page_num, chunk in relevant_chunks:
            prompt += f"Page {page_num}: {chunk}\n"
        prompt += f"\nQuestion: {query}"
        return query_gemini_llm(prompt)
    else:
        return "No relevant information found."

# Streamlit Application
def main():
    st.title("📄 Chat with Your PDF")
    st.write("Upload a PDF and ask specific questions about its content using the Gemini API.")
    
    # Step 1: Upload PDF
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    
    if uploaded_file is not None:
        st.write("Extracting text from PDF...")
        pdf_text_by_page = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")
        
        # Step 2: Chunk Text by Page
        st.write("Chunking text per page for better processing...")
        chunks = chunk_text_by_page(pdf_text_by_page)
        st.success(f"PDF text split into chunks by page.")
        
        # Step 3: User Query
        query = st.text_input("Ask a question about the uploaded PDF:")
        if query:
            st.write("Searching for relevant information...")
            
            # Step 4: Extract and Query
            if "unemployment" in query.lower():
                response = extract_unemployment_info(chunks, query)
            else:
                # For general queries, we will simply use chunks from the document
                relevant_chunks = "\n".join([f"Page {page_num}: {chunk[:300]}..." for page_num, chunk_list in chunks.items() for chunk in chunk_list[:3]])
                prompt = f"Based on the following context, answer the question:\n\n{relevant_chunks}\n\nQuestion: {query}"
                response = query_gemini_llm(prompt)
            
            st.write("### Response:")
            st.write(response)

if __name__ == "__main__":
    main()
