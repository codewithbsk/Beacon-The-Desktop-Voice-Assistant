
import datetime
from typing import Text
import pyttsx3
import speech_recognition 
from googletrans import Translator
import wikipedia
import pywhatkit
import re
import os
import speedtest
import pyautogui

eng= pyttsx3.init() 
#for female voice

v = eng.getProperty("voices")
eng.setProperty("voice",v[1].id)

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
        print("Processing...")
        query  = r.recognize_google(audio,language='hi')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Oops... Please check your Internet Connection...")
        # speak("क्षमस्व ")
        return "None"
    return query.lower()


def Translate(Text):
    translate = Translator()
    result = translate.translate(Text,dest ='hi')
    Text_res = result.text
    return Text_res


def int_to_hindi(num):
    # Define a dictionary of Hindi words for numbers
    hindi_nums = {
        0: 'शून्य',
        1: 'एक',
        2: 'दो',
        3: 'तीन',
        4: 'चार',
        5: 'पांच',
        6: 'छह',
        7: 'सात',
        8: 'आठ',
        9: 'नौ',
        10 : 'दस',
        11 : 'ग्यारह',
        12 : 'बारह',
        13 : 'तेरह',
        14 : 'चौदह',
        15 : 'पंद्रह',
        16 : 'सोलह', 
        17 : 'सत्रह',
        18 : 'अट्ठारह', 
        19 : 'उन्निस', 
        20 : 'बीस',
        21 : 'इक्कीस', 
        22 : 'बाईस',
        23 : 'तेईस',
        24 : 'चौबीस', 
        25 : 'पच्चीस',
        26 : 'छब्बीस',
        27 : 'सत्ताईस', 
        28 : 'अट्ठाईस', 
        29 : 'उनतीस', 
        30 : 'तीस',
        31 : 'इकतीस', 
        32 : 'बत्तीस' ,
        33 : 'तैंतीस' ,
        34 : 'चौंतीस' ,
        35 : 'पैंतीस' ,
        36 : 'छ्त्तीस' ,
        37 : 'सैंतीस' ,
        38 : 'अड़तीस' ,
        39 : 'उनतालीस' ,
        40 : 'चालीस' ,
        41 : 'इकतालीस', 
        42 : 'बयालीस',
        43 : 'तैंतालीस' ,
        44 : 'चौंतालीस' ,
        45 : 'पैंतालीस' ,
        46 : 'छियालीस' ,
        47 : 'सैंतालीस' ,
        48 : 'अड़तालीस' ,
        49 : 'उनचास' ,
        50 : 'पचास' ,
        51 : 'इक्याबन', 
        52 : 'बावन' ,
        53 : 'तिरेपन' ,
        54 : 'चौबन' ,
        55 : 'पचपन',
        56 : 'छप्पन', 
        57 : 'सत्तावन',
        58 : 'अट्ठावन', 
        59 : 'उनसठ',
        60 : 'साठ' ,
        2023: 'दो हजार तेयीस',
        2024: 'दो हजार चौबीस',

        # Add more numbers as needed
        # Add More Years as needed
    }
    digits = [int(d) for d in str(num)]
    # If the number is between 11-19 or is a multiple of ten, return the corresponding Hindi word
    if num in hindi_nums:
        hindi_words = hindi_nums[num]
    elif num < 100 and num % 10 == 0:
        hindi_words = hindi_nums[num]
    elif num < 100 and num > 20:
        hindi_words = hindi_nums[num//10*10] + ' ' + hindi_nums[num%10]
    else:
        # Convert each digit to its Hindi equivalent and join them
        hindi_words = ' '.join([hindi_nums[d] for d in digits])
    return hindi_words


def dateandtimehindi(arg):
    d = datetime.datetime.now()
    s = "सुबह के"
    hindi_date = int_to_hindi(d.day)
    hindi_year = int_to_hindi(d.year)
    hrs = int(d.hour)
    if arg == 1:
        if hrs > 11:
            if hrs < 16:
                s = "दोपहर के"
                if hrs > 12:
                    hrs = hrs - 12
            elif hrs < 20:
                s = "शाम के"
                hrs = hrs - 12
            else:
                s = "रात के"
                hrs = hrs - 12
        hindi_hour = int_to_hindi(hrs)
        hindi_minute = int_to_hindi(d.minute)
            
        TimeI = Translate("अभी समय " + s + " " + hindi_hour + " बजकर " + hindi_minute + " मिनट " + "है।") 
        return TimeI
    else:
        l = ["जनवरी", "फ़रवरी", "मार्च", "अप्रैल", "मई", "जून", "जुलाई", "अगस्त", "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"]
        DateI = Translate("आज की तारीख " + hindi_date + " " + l[int(d.month-1)] + " " + hindi_year + " है।")
        return DateI
  

def TaskExe():
    while True:
        global user
        queryHindi = TakeCommand()

        if ("हेलो" or "कैसे हो") in queryHindi:
            speak("मै अच्छा हुं सर, आप कैसे हो")

        elif('सो जाओ' in queryHindi) or ("शट डाउन" in queryHindi) or ("बंद" in queryHindi):
            import sys
            speak("ओकेय सर, बंद हो रहा हुं")
            sys.exit()

        #SCREENSHOT 
        elif("स्क्रीनशॉट" in queryHindi):
            speak("स्क्रीनशॉट ले रहा है")
            from screenshot import takeSS
            SS = takeSS()
            speak('कैप्चर किया गया स्क्रीनशॉट स्क्रीनशॉट फ़ोल्डर में सहेजा गया है।')
            del SS

        elif ("वेलकम" in queryHindi) or ("स्वागत" in queryHindi):
            speak("नैक मूल्यांकन समिति के सम्मानित सदस्यों का स्वागत है! यह बहुत खुशी की बात है कि हम आपकी कॉम्पुटर प्रयोगशाला में आपका स्वागत करते हैं, जहां आपको हमारे छात्रों द्वारा काम कर रहे कुछ सबसे नवीन और रोमांचक प्रोजेक्ट को देखने का अवसर मिलेगा । हमें उम्मीद है कि यहां आपकी यात्रा ज्ञानवर्धक और प्रेरक होगी, और आप हमारे छात्रों द्वारा अपनी प्रोजेक्ट में लगाए गए समर्पण और कड़ी मेहनत के लिए गहरी सराहना करेंगे।")

        elif "टाइम" in queryHindi or "समय" in queryHindi:
            time_hindi = dateandtimehindi(1)
            speak(time_hindi)

        elif "तारीख" in queryHindi or "":
            date_hindi = dateandtimehindi(0)
            speak(date_hindi)
   
        elif "जानकारी" in queryHindi:
            speak("विकिपीडिया पर जानकारी खोज रहे हैं")
            queryHindi = queryHindi.replace("खोजो","")
            queryHindi = queryHindi.replace("की","")
            queryHindi = queryHindi.replace("जानकारी","")
            queryHindi = queryHindi.strip() # Remove any leading or trailing spaces
            
            try:
                result = wikipedia.summary(queryHindi, sentences=3)
                speak("विकिपीडिया के अनुसार")
                ConHin = Translate(result)
                speak(ConHin)
            except wikipedia.exceptions.PageError:
                speak("माफ़ कीजिये, आपके खोजे हुए शब्दों से कोई पृष्ठ नहीं मिला")


        elif u"खोलो"in queryHindi or u"ओपन करो" in queryHindi:
            from Dictapp import openwebappHindi
            openwebappHindi(queryHindi)
        
        elif u"बंद करो" in queryHindi:
            from Dictapp import closeappwebHindi
            closeappwebHindi(queryHindi)

        elif "गूगल" in queryHindi:
            from searchNowHindi import searchGoogleHindi
            searchGoogleHindi(queryHindi)
      
        elif "सॉन्ग लगाओ" in queryHindi or "मुसिक लगाओ" in queryHindi:
            song = queryHindi.replace('सॉन्ग लगाओ', '').replace('मुसिक लगाओ', '').strip()
            queryHindi = "कृपया प्रतीक्षा करे , सोंग लागा रहे है"
            speak(queryHindi)
            speak('ये रहा आपका सोंग')
            pywhatkit.playonyt(song)

        elif ('बढ़िया' in queryHindi) or ('अच्छा' in queryHindi):
            speak("जानकर खुशी हुई सर ")

        elif ('बड़ा' in queryHindi):
            from Dictapp import maximizeApp
            speak('ओके कर रहा हुं')
            maximizeApp()

        elif ('छोटा' in queryHindi):
            from Dictapp import minimizeApp
            speak('ओके कर रहा हुं')
            minimizeApp()

        elif ("भाषा बदलो" in queryHindi) or ("लैंग्वेज" in queryHindi):
            import sys
            speak("ओकेय अभी भाषा, इंग्लिश मी बदल राहा हुं")
            v = eng.getProperty("voices")
            eng.setProperty("voice",v[0].id)
            speak("We are currently interacting in English , Please let me know how may i help you sir.")
            os.startfile("C:\\Users\\Bhalchandra Khedekar\\Desktop\\MAJOR PROJECT- BEACON\\mainsample2.py")
            sys.exit()
            
        elif ('नोट लिखो' in queryHindi):
        # 'take a note','note it down','make note','remember this as note','open notepad and write' in query):
            speak("आप क्या लिखना चाहेंगे सर?")
            data=TakeCommand()
            from noteHindi import note
            note(data)
            speak("मैंने इसका नोट बना लिया है।")

        #Playig random Music
        elif('म्यूजिक ' in queryHindi) or ('गाना' in queryHindi):
            speak("ओकेय सर, लगा रहा हुं")
            from play_music import play_music
            play_music()

        elif("फोटो"in queryHindi):
            from Automation import CameraHindi
            CameraHindi()
            speak('ओके सर, कैप्चर की गई फोटो , फोटोस फोल्डर में सेव हो गई है')
        
        elif "इंटरनेट की स्पीड" in queryHindi or "इंटरनेट का स्पीड" in queryHindi:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576
            print(f"वाईफाई अपलोड स्पीड है {round(upload_net, 2)} MBps")  # round() function is used to round off the result to 2 decimal places
            print(f"वाईफाई डाउनलोड स्पीड है {round(download_net, 2)} MBps")
            speak(f"वाईफाई डाउनलोड स्पीड है{round(download_net, 2)} Megabytes per second")
            speak(f"वाईफाई अपलोड स्पीड है {round(upload_net, 2)} Megabytes per second")
                        

        elif("मूवी" in queryHindi):
            speak("ठीक है एक मिनट रुकिए, मुझे यह जांचना है कि फिल्म आपके मूवी फोल्डर में मौजूद है या नहीं")
            from playMoviesHindi import play_movie
            play_movie(queryHindi)

        # Youtube Controls like Play, Pausme , Mute , Volume up and down 
        elif "पॉज वीडियो" in queryHindi or " रोको" in queryHindi:
            pyautogui.press("k")
            speak("वीडियो रोका गया")
        elif "प्ले वीडियो" in queryHindi or " चालू करो" in queryHindi:
            pyautogui.press("k")
            speak("वीडियो चलाया")
        elif "न्यूड वीडियो" in queryHindi or "म्यूट करो" in queryHindi:
            pyautogui.press("m")
            speak("वीडियो म्यूट किया गया")
        elif "अन म्यूट" in queryHindi or "अनु म्यूट करो" in queryHindi:
            pyautogui.press("m")
            speak("वीडियो अनम्यूट हो गया")

        elif "वॉल्यूम बढ़ाओ" in queryHindi:
            from keyboard1 import volumeup
            speak("वॉल्यूम बढ़ाया, सर")
            volumeup()
        elif "वॉल्यूम कम करो" in queryHindi:
            from keyboard1 import volumedown
            speak("वॉल्यूम कम किया, सर")
            volumedown()

        else:
            print("Oops...")
            # speak("क्षमस्व ")
        

TaskExe()
