import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    engine.say(text)
    engine.runAndWait()

    engine.stop()
    del engine

    time.sleep(0.5)