import PyPDF2
import docx
from odf import text, teletype
from odf.opendocument import load


def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text_data = ""
    for page in reader.pages:
        text_data += page.extract_text() or ""
    return text_data


def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def read_odt(file):
    doc = load(file)
    allparas = doc.getElementsByType(text.P)
    return "\n".join([teletype.extractText(p) for p in allparas])


def read_file(file, filename):
    if filename.endswith(".pdf"):
        return read_pdf(file)
    elif filename.endswith(".docx"):
        return read_docx(file)
    elif filename.endswith(".odt"):
        return read_odt(file)
    else:
        return file.read().decode("utf-8")
