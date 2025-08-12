# Climate Policy Analysis AI

A multi-agent AI system for analyzing, comparing, and recommending improvements for climate policies.

## Features
- Document analysis (PDF, DOCX, TXT)
- Policy comparison
- Recommendation generation
- Secure file handling

## Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Download Spacy model: `python -m spacy download en_core_web_sm`

## Usage
Run the Streamlit app:
```bash
streamlit run app/main.py