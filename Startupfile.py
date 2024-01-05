import os
import time
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen_to_me():
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        aud = r.listen(source)
    try:
        print('Processing...')
        aud = r.recognize_google(aud, language='en-in')
        print(f'User said : {aud}\n')
        return aud

    except Exception:
        print('Oops... Please check your Internet Connection...')
        speak("Sorry, I didn't get you. Please check your Internet Connection")
        return None


while True:

    command = listen_to_me()

    if command and ('wake up' in command or 'wake up beacon' in command):
        from GreetMe import greetMe
        greetMe()
        time.sleep(1)
        os.startfile('Give the Addrees of your Project like C:\\User\\')
        from Intro import play_gif
        play_gif()
        break

    else:
        print('Waiting for wake up command...')




 
