import re
import time
import pyttsx3
import speech_recognition


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,12)

    try:
        print("Processing..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Oops... Sorry, I didn't get you. Please check your Internet Connection...")
        # speak("Sorry, I didn't get you.")
        return "None"
    return query


def wait_Beacon():
    # listen for user input
    query = takeCommand()
    
    # extract the duration to wait from user input using regular expressions
    duration = None
    pattern = r"(\d+)\s+(minute|second)s?"
    match = re.search(pattern, query)
    if match:
        duration = int(match.group(1))
        if match.group(2) == "minute":
            duration *= 60

    # check if user wants to wait
    if duration:
        # wait for the specified duration
        print(f"Okay, I'll wait for {duration} seconds")
        speak(f"Okay, I'll wait for {duration} seconds")
        time.sleep(duration)
        print("Done waiting, sir")
        
    # continue with function execution
    print("Time up sir, i am waiting for your next query")
    speak("Time up sir, i am waiting for your next query")