import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"mspaint","microsoft word":"winword","excel":"excel","chrome":"chrome","vs code":"code",
           "powerpoint":"powerpnt","VLC ":"vlc","notepad":"notepad","photos":"ms-photos:",
           "google":"chrome https://www.google.com",
            "youtube":"chrome https://www.youtube.com",
            "facebook":"chrome https://www.facebook.com",
            "flipkart": "chrome https://www.flipkart.com",
            "amazon":"chrome https://www.amazon.com",
            "media player": "mediaplayer",
            "instagram": "chrome https://www.instagram.com",
            "whatsapp": "chrome https://web.whatsapp.com",
            "Camera" : "microsoft.windows.camera:",
            "word" : "winword",
            }


def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("beacon","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("One tab closed")
    elif "2 tab" in query or " two tabs" in query or "to tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Two tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Three tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Four tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Five tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                # import subprocess

                # # Find the process ID of PowerPoint
                # output = subprocess.check_output([f'tasklist', '/fi', f'imagename eq {dictapp[app]}.EXE'])
                # process_ids = [int(line.split()[1]) for line in output.splitlines()[3:]]

                # # Kill each instance of PowerPoint
                # for process_id in process_ids:
                #     subprocess.call(['taskkill', '/F', '/T', '/PID', str(process_id)])

                os.system(f"taskkill /f /im {dictapp[app]}.exe")



# define the app and website mappings for Hindi language
hindi_app_map = {
    "कमांड प्रॉम्प्ट": "cmd",
    "पेंट": "mspaint",
    "वर्ल्ड ": "winword",
    "एक्सएल": "excel",
    "क्रोम": "chrome",
    "रुम": "chrome",
    "वीएस कोड": "code",
    "पावरप्वाइंट": "powerpnt",
    "और": "powerpnt",
    "वीएलसी ": "vlc",
    "नोटपैड": "notepad",
    "नोट": "notepad",
    "फोटोस": "ms-photos:",
}

def openwebappHindi(queryHindi):
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate",150)
    # determine the app/website mapping based on the language
    if ".com" in queryHindi or ".co.in" in queryHindi or ".org" in queryHindi:
        queryHindi = queryHindi.replace("खोलो","")
        queryHindi = queryHindi.replace("","")
        queryHindi = queryHindi.replace("","")
        queryHindi = queryHindi.replace(" ","")
        webbrowser.open(f"https://www.{queryHindi}")
        speak("वेबसाइट खोल रहा हूँ")
    else:
        # iterate over the app map to find a matching keyword
        for keyword in hindi_app_map:
            if keyword in queryHindi:
                app_name = hindi_app_map[keyword]
                speak("खोल रहा हुं सर")
                os.system(f"start {app_name}")
                #speak(f"{app_name}")
               
                break
        else:
            speak("माफ़ कीजिए, मुझे उस ऐप या वेबसाइट के बारे में पता नहीं है")


def closeappwebHindi(queryHindi):
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate",150)
    speak("बंद कर रहा हुं सर")
    if "एक टैब" in queryHindi or "1 tab" in queryHindi:
        pyautogui.hotkey("ctrl","w")
        speak("एक टैब बंद कर रहा हुं सर")
    elif "2 tab" in queryHindi or " दो टैब" in queryHindi or "to tabs" in queryHindi:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("दो टैब बंद कर रहा हुं सर")
    # elif "तीन टैब" or "3 टैब" in queryHindi:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("तीन टैब बंद कर रहा हुं सर")
        
    # elif "चार टैब" or"4 टैब " in queryHindi:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("चार टैबकर बंद कर रहा हुं सर")
    # elif "पाच टैब" or"5 टैब" in queryHindi:
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     sleep(0.5)
    #     pyautogui.hotkey("ctrl","w")
    #     speak("पाच टैबकर बंद कर रहा हुं सर")

    else:
        for keyword in hindi_app_map:
            if keyword in queryHindi:
                os.system(f"taskkill /f /im {hindi_app_map[keyword]}.exe")
        
        # for keyword in hindi_app_map:
        #     if keyword in queryHindi:
        #         if "टैब" in queryHindi or "tab" in queryHindi:
        #             os.system(f"taskkill /f /im {hindi_app_map[keyword]}.exe")
        #         else:
        #             os.system(f"start {hindi_app_map[keyword]}.exe")

def maximizeApp():
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')

def minimizeApp():
    pyautogui.hotkey('win', 'down')
              
                
        