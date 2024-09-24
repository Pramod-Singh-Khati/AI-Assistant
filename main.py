import speech_recognition as sr
import os
import pyautogui
import webbrowser
import win32com.client
import wikipedia
import cv2
import datetime
import threading
import random
import pywhatkit as kit
from requests import get
from chat import Brain
from camera import mouse
from clap import MainClap
from virtualmouse import virtual_mouse
speaker = win32com.client.Dispatch("SAPI.SpVoice")
MainClap()

def say(text):

    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         #r.pause_threshold =0.6
         #r.energy_threshold =300
         audio = r.listen(source)
         try:
             print("Recognizing...")
             query = r.recognize_google(audio, language="en-in")
             print(f"User said: {query}")
             return query
         except Exception as e:
             return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':

    print("Hello Mr. Pramod, I am jarvis ,How can i assist you , sir")
    say("Hello Mr. Pramod, I am jarvis ,How can i assist you , sir")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        '''sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])'''
        # todo: Add a feature to play a specific song


        if 'wikipedia' in query.lower():
            print('Searching Wikipedia...')
            say("Searching Wikipedia sir")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            say("Acording to wikipedia sir")
            print(results)
            say(results)

        elif "open youtube" in query.lower():
            say("Opening Youtube sir")
            webbrowser.open("https://www.youtube.com")

        elif "close youtube" in query.lower():
            pyautogui.hotkey("ctrl", "w")
            say("youtube terminated")

        elif "open google" in query.lower():
            say("Opening Google sir")
            webbrowser.open("https://www.google.com")


        elif 'search' in query.lower():
            print('Searching Google...')
            say("sir, what should i search on google")
            cm = takeCommand().lower()
            say(f"Searching {cm} sir")
            webbrowser.open(f"{cm}")



        elif "open camera" in query:
            camera = cv2.VideoCapture(0)
            say("Opening Camera sir")
            while True:
                ret, frame = camera.read()
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            camera.release()
            cv2.destroyAllWindows()



        elif "open spotify" in query:
            say("Opening Spotify sir")
            musicPath = 'C:\\Users\\AKHILESH\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(musicPath)

        elif "close spotify" in query:
            say("spotify terminated")
            os.system(f"taskkill /f /im spotify.exe")

        elif "open mouse".lower() in query.lower():
            say("Opening Mouse sir")
            mouse()

        elif "open virtual camera".lower() in query.lower():
            say("virtual carmer mode activated")
            virtual_mouse()

        elif 'play music' in query:
            say("Playing music sir")
            music_dir = 'D:\\music\\favorite songs'  # File Path
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
            os.startfile(os.path.join(music_dir, rd))

        elif "the time" in query:

            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "ip address" in query.lower():
            say("Getting IP address sir")
            ip = get('https://api.ipify.org').text
            print(ip)
            say(f"Your IP address is {ip} sir")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Some Error Occurred. Sorry from Jarvis".lower() in query.lower():

            print("...")

        elif "Jarvis Quit".lower() in query.lower():
            say("Thank you sir, have a nice day!")
            exit()

        else:
            print("Chating...")
            chat = Brain(query)

            say(chat)




