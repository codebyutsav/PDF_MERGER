from pypdf import PdfWriter

merger = PdfWriter()
pdfs=[]

num=int(input("How many PDFs you want to merge? "))

for i in range(0,num):
    user_input=input(f"Enter the name of PDF {i + 1} : ")
    pdfs.append(user_input)


for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()