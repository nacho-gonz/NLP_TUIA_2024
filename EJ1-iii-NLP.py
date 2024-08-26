from docx import Document

doc = Document(r'Archivos\word.docx')

par = 0

for parrafo in doc.paragraphs:
    print(parrafo.text)
    par += 1
    if par == 15:
        break