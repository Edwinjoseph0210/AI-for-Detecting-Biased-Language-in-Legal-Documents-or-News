from docx import Document

def read_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs]) 