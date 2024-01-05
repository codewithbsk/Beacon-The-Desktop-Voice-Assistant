import os
import pyautogui
import time 
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

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

def takeCommandHindi():
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


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def MaximizeVsCode():
    pyautogui.click(x=1510, y=74)
    
       
def MinimizeVsCode():
    pyautogui.click(x=1452, y=78) 
    
def Camera():
    speak("okay sir, hold on opening camera")
    os.system("start microsoft.windows.camera:")
    speak("Are you ready to take picture sir") 
    a = takeCommand()
    if 'yes' in a.lower() or 'ready' in a.lower() or 'take' in a.lower:
        pyautogui.click(1886, 542)
    else:
        speak("Waiting for few seconds. Be ready to click photo sir.")
        time.sleep(10)
        speak("Can I take photo now?")
        a = takeCommand()
        if 'yes' in a.lower() or 'can' in a.lower() or 'take' in a.lower:
            pyautogui.click(1886, 542)

def CameraHindi():
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    speak("ठीक है सर, रुकिए ,कैमरा खोल रहा हुं ")
    os.system("start microsoft.windows.camera:")
    speak("क्या आप तस्वीर लेने के लिए तैयार हैं सर") 
    a = takeCommandHindi()
    if 'हा' in a or 'हां' in a or "ले सकते हो" in a or "हां तैय्यार हुं" in a or ("खिचो"):
        pyautogui.click(1886, 542)
    else:
        speak("कुछ सेकंड प्रतीक्षा कर रहा हुं,। फोटो क्लिक करने के लिए तैयार रहिये सर")
        time.sleep(10)
        speak("क्या मैं अभी फोटो खींच सकता हूँ सर?")
        a = takeCommand()
        if 'हा' in a or 'हां' in a or "ले सकते हो" in a or "हां खिचो" in a or "खींच सकते हो" in a:
            pyautogui.click(1886, 542)


