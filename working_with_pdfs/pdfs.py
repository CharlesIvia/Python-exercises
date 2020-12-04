import PyPDF2
from PyPDF2 import pdf

#Reading pdfs

f = open("Working_Business_Proposal.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(f)

pages = pdf_reader.numPages
print(pages)

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()
print(page_one_text)

f.close()

#Adding page to pdf file

f = open("Working_Business_Proposal.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(f)

page_one = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)

pdf_output = open("New_Proposal.pdf", "wb")

pdf_writer.write(pdf_output)

f.close()
pdf_output.close()

#Etract all text

f = open("Working_Business_Proposal.pdf", "rb")

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text)