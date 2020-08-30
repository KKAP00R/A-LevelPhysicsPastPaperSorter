# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('20162.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

i= 0
while i<pdfReader.numPages:
    pageObj = pdfReader.getPage(i)
    i+=1
    print(pageObj.extractText()) 
 

# closing the pdf file object 
pdfFileObj.close() 
