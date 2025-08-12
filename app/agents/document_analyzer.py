import spacy
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader
from docx import Document
import re

nlp = spacy.load("en_core_web_sm")

class DocumentAnalyzer:
    def __init__(self):
        self.nlp = nlp

    def extract_text(self, file_path):
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = '\n'.join([page.extract_text() for page in reader.pages])
            
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])

        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
        return text
    
    def analyze_policy(self, text):
        doc = self.nlp(text)

        # Extract key entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Extract key sentences
        sentences = sent_tokenize(text)
        key_sentences = [sent for sent in sentences if any(
            kw in sent.lower() for kw in ['climate', 'policy', 'target', 'emission', 'carbon']
        )]

        # Extract policy targets (simplified)
        targets = re.findall(r'reduce\s+by\s+(\d+%)', text, re.IGNORECASE)

        return {
            'entities': entities,
            'key_sentences': key_sentences,
            'targets': targets,
            'summary': self.generate_summary(text)
        }
    
    def generate_summary(self, text, max_sentences=3):
        sentences = sent_tokenize(text)
        if len(sentences) <= max_sentences:
            return " ".join(sentences)
        
        # Simple summary - first and last sentences
        return " ".join([sentences[0], sentences[-1]])