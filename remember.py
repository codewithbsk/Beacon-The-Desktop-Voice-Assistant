import speech_recognition as sr
import pyttsx3

engine =pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def rememberThat():
    remember =''
    speak("What do you want to remember sir:")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio).lower()
        print(f"You said: {remember}")
        rememberMessage = query.replace("remember that","")
        rememberMessage = query.replace("beacon","")
        speak("You told me to remember that"+rememberMessage)
        remember = open("Remember.txt","a")
        remember.write(rememberMessage)
        remember.close()
        speak("Okay sir, remembered")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't get that. Please try again.")
        return

