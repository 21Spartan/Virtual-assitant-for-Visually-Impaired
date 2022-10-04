import pytesseract as pes
import pyttsx3

def read():
    pes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    from PIL import Image
    img = Image.open('amn.jpg')
    text = pes.image_to_string(img)
    print(text)
    Filename='kpn.txt'
    with open(Filename,'w') as fileObj:
        fileObj.write(text)

    py = pyttsx3.init()
    voices = py.getProperty('voices')
    fo = open("kpn.txt","r")
    ab = fo.read()
    fo.close()
    py.setProperty("rate",200)#for speed
    py.setProperty("voice",voices[1].id)#for male voice[0]
    py.setProperty("volume",1)#for volume
    py.say(ab)
    py.runAndWait()
