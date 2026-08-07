from modules import Sites
import webbrowser
from datetime import datetime
import psutil
from modules import volume_control
import os
from modules import music
from modules import ai
from modules import apps
from modules import wiki
import pyttsx3
import time
from modules import weather
from modules import news

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    engine.say(text)
    engine.runAndWait()

    engine.stop()
    del engine

    time.sleep(0.5)

def route(command):

    for key in Sites.sites:
        if f"open {key}" in command:
            a = f"opening {key}"
            speak(a)
            webbrowser.open(Sites.sites[key])
            break

    if "search google for" in command:
        speak("Searching google")
        query = command.split("search google for") # to remove search google from command
        Sites.search_google(query[1])

    elif "search youtube for" in command:
        speak("Searching youtube")
        query = command.split("search youtube for") # to remove search youtube for from command
        Sites.search_youtube(query[1]) 

    elif "what's the time" in command or "what is time" in command or "tell me time" in command:
        now = datetime.now()
        print(now.strftime("Current time is %I:%M %p"))
        c = now.strftime("Current time is %I:%M %p")
        speak(c)

    elif "what is the date today" in command or "tell me date" in command or "what's the date" in command:
        now = datetime.now()
        print(now.strftime("Today is %A %d %B %Y"))
        b = now.strftime("Today is %A %d %B %Y")
        speak(b)

    elif "tell me current date and time" in command or "tell me date and time" in command or "what's the date and time" in command:
        now = datetime.now()
        print(now.strftime("Today is %A %d %B %Y"),now.strftime("current time is %I:%M %p"))
        c = (
    now.strftime("Today is %A %d %B %Y")
    + " "
    + now.strftime("Current time is %I:%M %p")
)
        speak(c)



    elif "battery percentage" in command or "tell me battery percentage" in command or "what's the battery percentage" in command:
        battery = psutil.sensors_battery()
        print(f"Your battery is at {battery.percent} percent")
        speak(f"Your battery is at {battery.percent} percent")

    elif "increase volume" in command:
        speak("increasing volume")
        volume_control.volume_up()

    elif "decrease volume" in command:
        speak("decreasing volume")
        volume_control.volume_down()


    

    elif "shut down pc" in command or "shutdown pc" in command:
        speak("Shutting down laptop")
        os.system("shutdown /s /t 5")

    elif "restart pc" in command or "restart laptop" in command:
        speak("Restarting laptop")
        os.system("shutdown /r /t 5")

    elif "sleep pc" in command or "sleep laptop" in command:
        speak("sleeping laptop")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    elif "play music" in command or "play songs" in command:
        speak("playing music")
        music.play_random_song()

    elif "ask ai" in command:
        query = command.split("ask ai")
        answer = ai.ask_ai(query[1])
        speak(answer)
        print(answer)

    elif "open app" in command:
        speak("opening application")
        if not apps.open_app(command):
            print("Application not found.")

    elif "wiki" in command:
        topic = command.replace("wiki", "").strip()
        if topic:
            result = wiki.search_wikipedia(topic)
            print(result)
            speak(result)

    elif "weather in" in command:
        city = command.split("weather in", 1)[1].strip()

        if city:
            result = weather.get_weather(city)
            print(result)
            speak(result)

    elif "latest news" in command or command == "news":
        speak("Getting the latest news")
        headlines = news.get_news()
        if isinstance(headlines, list):
            for i, headline in enumerate(headlines, 1):
                print(f"{i}. {headline}")
                speak(headline)
        else:
            print(headlines)
            speak(headlines)