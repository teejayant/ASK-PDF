import PyPDF2  # Import the PyPDF2 library for PDF file handling


# page extraction function
import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object to read the PDF file
    text = ""  # Initialize an empty string to store extracted text

    for page_num, page in enumerate(reader.pages, start=1):  # Loop with page number (starting from 1)
        content = page.extract_text()  # Extract text from the current page
        if content:  # Check if any text was extracted
            text += f"\n--- Page {page_num} ---\n"  # Add page number as a header
            text += content + "\n"  # Add the extracted text/content to the result string

    return text  # Return the combined text

