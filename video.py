import cv2
import time
import pyttsx3

def detect():
    engine =  pyttsx3.init()
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[1].id)
            #Create our body classifier
    car_classifier = cv2.CascadeClassifier('car.xml')
    path='second.mp4'
    cap = cv2.VideoCapture('second.mp4')
    fgbg = cv2.createBackgroundSubtractorMOG2()
    cap

    def talk(audio):
        engine.say(audio)
        engine.runAndWait()

    while True:
        ret, img = cap.read()
        fgbg.apply(img)
        if (type(img) == type(None)):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cars = car_classifier.detectMultiScale(gray, 1.1, 2)

        for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            talk("There is a car")


    cv2.imshow('video', img)


    if cv2.waitKey(33) == 27:

        break


    cv2.destroyAllWindows()


