# Task-1-Chat-with-PDF-Using-RAG-Pipeline
# 📄 PDF Chat with Gemini API

This project allows users to upload a PDF and ask questions about its content using the Gemini API by Google. The application extracts text from the uploaded PDF, splits it into chunks for efficient processing, and then uses the Gemini API to generate responses based on the content of the document.

## Features

- **PDF Upload**: Upload PDF files to the app.
- **Text Extraction**: Extracts and processes the content of the PDF using PyMuPDF.
- **Text Chunking**: Splits the extracted text into chunks for easier querying.
- **Gemini API Integration**: Leverages the Gemini API for querying the document and generating answers.
- **User Interface**: Built with Streamlit, providing an easy-to-use interface for interacting with the PDF.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository or download the code.

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd Task-1-Chat-with-PDF-Using-RAG-Pipeline
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

   The `requirements.txt` file contains the following dependencies:

   - `pymupdf`: For extracting text from PDF files.
   - `google-generativeai`: To interact with the Gemini API.
   - `streamlit`: For building the web interface.

## Setup

1. **Gemini API Key**: You will need to set up a Gemini API key for the application to interact with Google's generative models.

    - Replace the value of `GEMINI_API_KEY` in the `app.py` file with your own Gemini API key:

    ```python
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
    ```

2. **Running the Application**: 

    To run the Streamlit app, execute the following command:

    ```bash
    streamlit run app.py
    ```

    This will start the app in your web browser where you can upload PDFs and ask questions related to the content.

## How It Works

1. **Upload PDF**: Upload a PDF document using the file uploader.
2. **Extract and Chunk Text**: The text from the PDF is extracted and chunked for easier querying.
3. **Ask Questions**: You can then ask specific questions about the content of the PDF.
4. **Get Answers**: The app will query the Gemini API with relevant chunks from the PDF to generate a response.

For example:
- **User Query**: "From page 2, get the exact unemployment information based on type of degree input."
- **Response**: The app will search through the document, find relevant content about unemployment, and generate an answer using the Gemini API.


## Acknowledgements

- The app uses **PyMuPDF** for PDF text extraction.
- The **Gemini API** by Google is used for generating responses based on the document content.
- **Streamlit** is used to build the web interface for easy interaction.

