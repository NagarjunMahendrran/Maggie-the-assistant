import speech_recognition as sr
import webbrowser
import pyttsx
import time
import _functions
import thread
from _functions import *
from pygame import mixer

mixer.init()
mixer.music.load("/home/tch/Downloads/arjun_dhanu_project/bootup.mp3")
mixer.music.play()

while True:
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source,phrase_time_limit=2)
  try:
    print("You said: " + r.recognize_google(audio))
    dhanu_main_thread(r.recognize_google(audio))
  except sr.UnknownValueError:
    print("I am waiting for your command boss!")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
time.sleep(.1)
