from gtts import gTTS
import PyPDF2


book = open('Novel.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages


for num in range(25, pages):
    page = pdfReader.getPage(num)
    page_text = page.extractText()
    language = 'en'
    myobj = gTTS(text=page_text, lang=language, slow=False)
    myobj.save("D:/test"+str(num)+".mp3")