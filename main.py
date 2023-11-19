import pyttsx3
import PyPDF2

path = r"Book.pdf"
pdf_file = open(path, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

speaker = pyttsx3.init()

# Female Voice
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

for page_num in range(len(pdf_reader.pages)):
    # page = pdf_reader.getPage(page_num)
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

pdf_file.close()
