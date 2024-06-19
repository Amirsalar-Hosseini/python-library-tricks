from pdf2docx import Converter
cv = Converter ('wordd.pdf')
cv.convert('wordddd.docx', start=0, end=None)
cv.close()