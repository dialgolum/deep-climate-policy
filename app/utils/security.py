import re

class Security:
    @staticmethod
    def sanitize_input(text):
        # Remove potentially harmful characters
        sanitized = re.sub(r'[;|&$<>]', '', text)
        return sanitized.strip()
    
    @staticmethod
    def validate_file_extension(filename, allowed_extensions=['.pdf', '.docx', '.txt']):
        return any(filename.endswith(ext) for ext in allowed_extensions)