import speech_recognition as sr
from speak import *
import os
from PIL import Image
from txttohand import *

r = sr.Recognizer()

def speech():
    with sr.Microphone() as source:
        print('Say Something')
        male("say something")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        print("Did you say this (Yes/No) : ")
        male("Did you say"+ text + "(please answer in Yes or No)")
        a = r.listen(source)
        answer = r.recognize_google(a)
        if (answer == "Yes" or answer == "yes"):
            print("Thanks, I've got it from here")
            male("Thanks, I've got it from here")
            try:
                input_out(text)
            except:
                pass
        else:
            speech()

def typing(text):
    print("Thanks, I've got it from here")
    male("Thanks, I've got it from here")
    try:
        input_out(text)
    except:
        pass


      
        