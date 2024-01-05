import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey= Your API KEY",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey= Your API KEY",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey= Your API KEY",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey= Your API KEY",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey= Your API KEY",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey= Your API KEY"
    }

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        field = r.recognize_google(audio).lower()
        print(f"You said: {field}")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't get that. Please try again.")
        return

    for key ,value in api_dict.items():
        if key.lower() in field:
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Do you want to listen to another news?")
            print("Listening...")
            audio = r.listen(source)

        try:
            a = r.recognize_google(audio).lower()
            print(f"You said:{a}")
            if "yes" in a:
                latestnews()
                        
            elif "no" in a:
                speak("Okay, no problem. Have a good day!")
                break
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            a = r.recognize_google(audio).lower()
            print(f"You said:{a}")
            if "yes" in a:
                latestnews()
                        
            elif "no" in a:
                speak("Okay, no problem. Have a good day!")
                break



