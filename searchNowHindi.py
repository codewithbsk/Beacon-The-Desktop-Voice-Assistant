import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from googletrans import Translator


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)


eng= pyttsx3.init() 

def Translate(Text):
    translate = Translator()
    result = translate.translate(Text,dest ='hi')
    Text_res = result.text
    return Text_res


def speak(audio):
    print(" ")
    print(f": {audio}")
    eng.say(audio)
    eng.runAndWait()
    print(" ")

def TakeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Processing..")
        query  = r.recognize_google(audio,language='hi')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Oops... Please check your Internet Connection...")
        # speak("क्षमस्व ")
        return "None"
    return query.lower()




def searchGoogleHindi(queryHindi):
    if "गूगल" in queryHindi:
        import wikipedia as googleScrap
        queryHindi = queryHindi.replace("jarvis","")
        queryHindi = queryHindi.replace("google search","")
        queryHindi = queryHindi.replace("गूगल","")

        try:
            pywhatkit.search(queryHindi)
            result = googleScrap.summary(queryHindi,2)
            speak("यह मैंने गूगल पर पाया")
            ConEng = result
            ConHin = Translate(ConEng)
            speak(ConHin)

        except:
            speak("No speakable output available")








