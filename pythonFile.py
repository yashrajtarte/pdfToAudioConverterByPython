import PyPDF2
import pyttsx3

# insert name of your pdf
# insert name of your pdf
pdfreader = PyPDF2.PdfReader("The Buddha and the Badass.pdf")
speaker = pyttsx3.init()

for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)
# name mp3 file whatever you would like
speaker.save_to_file(clean_text, "The Buddha and the Badass.mp3")
speaker.runAndWait()
speaker.stop()
