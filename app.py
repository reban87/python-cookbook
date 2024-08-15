import streamlit as st
import json
import base64
import io


def generate_pdf_from_base64(json_data):
    # Parse the JSON string
    parsed_data = json.loads(json_data)

    # Process each item in the parsed data
    for item in parsed_data:
        filename = item["filename"]
        pdf_data = item["pdf_data"]

        # Decode the base64 string
        decoded_pdf = base64.b64decode(pdf_data)

        # Create a BytesIO object
        pdf_bytes = io.BytesIO(decoded_pdf)

        # Create a download button for the PDF
        st.download_button(
            label=f"Download {filename}",
            data=pdf_bytes,
            file_name=filename,
            mime="application/pdf",
        )


# Streamlit app
st.title("PDF Generator from Base64 Data")

# Text area for JSON input
json_input = st.text_area("Enter your JSON data here:", height=200)

if st.button("Generate PDFs"):
    if json_input:
        try:
            generate_pdf_from_base64(json_input)
        except json.JSONDecodeError:
            st.error("Invalid JSON data. Please check your input.")
    else:
        st.warning("Please enter some JSON data.")

# Instructions
st.markdown(
    """
### Instructions:
1. Paste your JSON data containing base64 encoded PDFs into the text area above.
2. Click the "Generate PDFs" button.
3. Download buttons will appear for each PDF in the JSON data.
4. Click on each button to download the corresponding PDF.

### Expected JSON format:
```json
[
    {
        "filename": "example1.pdf",
        "analysis": "Some analysis",
        "pdf_data": "base64_encoded_pdf_data_here"
    },
    {
        "filename": "example2.pdf",
        "analysis": "Some other analysis",
        "pdf_data": "another_base64_encoded_pdf_data_here"
    }
]
```
"""
)
