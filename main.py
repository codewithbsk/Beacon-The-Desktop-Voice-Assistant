import time
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pywhatkit
from googletrans  import Translator
from typing import Text
from play_music import play_music
import re
from setalarm import set_alarm
import random
import webbrowser
import speedtest
from plyer import notification
from pygame import mixer
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",150)
 
user =""

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
        print("Processing...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
        
    except Exception as e:
        print("Oops... Sorry, I didn't get you. Please check your Internet Connection...")
        # speak("Sorry, I didn't get you.")
        return "None"
    return query
    
    
def dateandtime(arg):
    d=datetime.datetime.now()
    s="am"
    hrs=int(d.hour)
    if(arg==1):
        if(hrs>11):
            s="pm"
            if(hrs>12):
                hrs=hrs-12
        return("Current time is "+str(hrs)+":"+str(d.minute)+" "+s)
    else:
        l=["January","February","March","April","May","June","July","August","September","October","November","December"]
        return("Current date is "+str(d.day)+" "+l[int(d.month-1)]+", "+str(d.year))


def Translate(Text):
    translate = Translator()
    result = translate.translate(Text,dest ='hi')
    Text_res = result.text
    return Text_res

if __name__ == "__main__":

            while True:
                query = takeCommand().lower()
                if "go offline" in query:
                    speak("Ok sir , You can call me anytime")
                    query = takeCommand().lower()
                    if "wake up" in query:
                        from GreetMe import greetMe
                        greetMe()


                if ("shutdown" in query) or ("sleep" in query) or ('shut down' in query):
                    speak("Okay sir, shutting down")
                    break 

                if (("great" in query) or ("nice" in query) or ("thank you" in query) or ("help" in query) or ("best"in query)):
                    i=random.randint(1,5)
                    if(i==1):
                        query="Your kind words mean a lot to me. It's an honor to assist you."
                    elif(i==2):
                        query="I'm grateful to be a part of your life and to have the opportunity to help you."
                    elif(i==3):
                        query="It's an absolute pleasure to assist you. Thank you for making my job so fulfilling."
                    elif(i==4):
                        query="I'm grateful for the opportunity to assist you and appreciate your recognition of my efforts. Thank you for being an amazing user."
                    elif(i==5):
                        query="I'm humbled by your kind words. Thank you for making my day."
                    print(query)
                    speak(query)

                if "welcome" in query or "committee" in query in "guest" in query:
                    speak("Welcome, honored members of the NAAC evaluation committee! It is with great pleasure that we welcome you to our project laboratory   , where you will have the opportunity to witness some of the most innovative and exciting projects our students have been working on  . We hope that your visit here will be enlightening and inspiring  , and that you will leave with a deeper appreciation for the dedication and hard work that our students have put into their projects.")

                if re.search(r'\bwho\b.*\bmade\b.*\byou\b', query, re.IGNORECASE):
                    response = "I was created by a team of developers as part of a group project. We worked together to design and build me to be a helpful digital assistant for our users. While I can't attribute my creation to just one person, I'm constantly learning and improving thanks to the contributions of my entire team."
                    print(response)
                    speak(response)

                else:
                    # if((("who" in query)or("are" in query))or((("what" in query)or("whats" in query)or("tell me" in query))and("your" in query)and("name" in query) and ("about"in query) and ("yourself"in query))):

                    #     query="Hello, I'm Beacon, your personal digital assistant. I'm here to help you with anything you need, from setting reminders to checking the weather. As an AI-powered assistant, I'm constantly learning and improving to better meet your needs. Whether you need help with work, home, or anything in between, I'm here for you. And, just so you know, I'm fluent in Hindi as well, so feel free to ask me anything in either language."
                    #     print(query)
                    #     speak(query)

                    if re.search(r'\b((who|what)\b.*\b(are|is)\b.*\byou\b|\btell me about yourself\b|\byourself\b.*\babout\b|\bwhat\'?s your name\b)', query, re.IGNORECASE):
                        response = "Hello, I'm Beacon, your personal digital assistant. I'm here to help you with anything you need, from taking photo to checking the weather. As an AI-powered assistant, I'm constantly learning and improving to better meet your needs. Whether you need help with work, home, or anything in between, I'm here for you. And, just so you know, I'm fluent in Hindi as well, so feel free to ask me anything in either language."
                        print(response)
                        speak(response)

                    elif(("who am i" in query)or((("what" in query)or("whats" in query)or("tell me" in query))and("my" in query)and("name" in query))):
                        if(user==""):
                            query="I'm sorry, I have no idea about you. Perhaps I would like to know your name, tell me your name?"
                            print(query)
                            speak(query)
                            while(1):
                                print("Speak your name:- ")
                                name=takeCommand()
                                if(name!="0"):
                                    if("nope" in name)or("don't" in name)or("leave" in name):
                                        query="Okay okay... Take it easy"
                                        print(query)
                                        speak(query)
                                        break
                                    else:
                                        user=name
                                        temp=random.choice((1,2,3))
                                        if(temp==1):
                                            query=name.capitalize()+". Very wise name."
                                        elif(temp==2):
                                            query="I'll remember your name "+name.capitalize()
                                        else:
                                            query=name.capitalize()+". Thats a fantastic name."
                                        print(query)
                                        speak(query)
                                        f=open("config_file.txt","w")
                                        f.write(user.capitalize())
                                        f.close()
                                        break
                                else:
                                    speak("tell me your name please")
                        else:
                            query="Your name is "+user.capitalize()
                            print(query)
                            speak(query)

                    elif("wait" in query):
                        speak("how many seconds or minutes do you wanna wait")
                        from waitBeacon import wait_Beacon
                        wait_Beacon()

                    #Hello, How are you
                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine what about you" in query or "i am great what about you" in query:
                        speak("I am an AI digital assistant, so I don't have feelings like humans do, but I'm always ready and available to assist you with any task you need help with. How can I assist you today?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("I am an AI digital assistant, so I don't have feelings like humans do, but I'm always ready and available to assist you with any task you need help with. How can I assist you today?")
                    elif ("what about you" in query):
                        speak("I am an AI digital assistant, so I don't have feelings like humans do, but I'm always ready and available to assist you with any task you need help with. How can I assist you today?")

                    #Opening the installed apps
                    elif "open" in query:
                        from Dictapp import openappweb
                        openappweb(query)
                    #Closing the installed apps
                    elif "close" in query:
                        from Dictapp import closeappweb
                        closeappweb(query)

                    elif "google" in query:
                        from SearchNow import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        from SearchNow import searchYoutube
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(query)
                    
                    elif "temperature" in query:
                        search = "temperature in devrukh"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current {search} is {temp}")
                        print(f"current {search} is {temp}")
                        
                    elif "weather" in query:
                        search = "wheather in devrukh"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current {search} is {temp}")
                        print(f"current {search} is {temp}")

                    elif("current" in query):
                        if("time" in query):
                            query=dateandtime(1)
                            print(query)
                            speak(query)
                        elif("date" in query):
                            query=dateandtime(0)
                            print(query)
                            speak(query)
                        else:
                            print("Oops")
                            speak("Sorry, I didn't get that")

                    elif ("set an alarm" in query) or ("set alarm" in query):   
                            speak("What time do you want to set the alarm for?")
                            text = takeCommand()
                            if text:
                                match = re.search(r'(\d{1,2})\D+(\d{2})\D*(am|pm)?', text.lower()) # Extract hour, minute, and am/pm components using regular expression
                                if match:
                                    hour = int(match.group(1))
                                    minute = int(match.group(2))
                                    if match.group(3) and match.group(3).lower() == 'pm' and hour != 12:
                                        hour += 12
                                    elif match.group(3) and match.group(3).lower() == 'am' and hour == 12:
                                        hour = 0
                                    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                                        speak("Sorry, that's not a valid time.")
                                    else:
                                        from setalarm import set_alarm
                                        set_alarm(hour,minute)
                        
                                else:
                                    speak("Sorry, I didn't understand the time.")
                                
                    elif ("minimise" in query) or ("minimize" in query) or ("minimised" in query):
                        speak("okay minimising")
                        from Dictapp import minimizeApp
                        minimizeApp()

                    elif ("maximise" in query) or ("maximize" in query) or ("maximised" in query):
                        speak("okay maximising")
                        from Dictapp import maximizeApp
                        maximizeApp()
                    
                    elif("play" in query) and ("song" in query):
                        speak("Okay wait a minute, i have to check ,that song is present in your song folder ,or not")
                        from playSong import play_song
                        play_song(query)
                        # song = query.replace('play', '').replace('song', '').strip()
                        # query = "Ok, wait a minute. Playing " + song + " song."
                        # speak(query)
                        # pywhatkit.playonyt(song)
                    
                    # elif("play" in query) and ("movie" in query):
                    #     song = query.replace('play', '').replace('movie', '').strip()
                    #     query = "Ok, wait a minute. Playing " + song + " movie."
                    #     speak(query)
                    #     pywhatkit.playonyt(song)

                    elif(("change language" in query)):
                        speak("Okay Changing Language to Hindi")
                        print("Okay Changing Language to Hindi")
                        v = engine.getProperty("voices")
                        engine.setProperty("voice",v[1].id)
                        speak("हेलो, में आपकी क्या मदत कर सकता हुं ? ")
                        print("हेलो, में आपकी क्या मदत कर सकता हुं ? ")
                        from hindi import TakeCommand
                        TakeCommand()
                        from hindi import TaskExe
                        TaskExe()

                    #Making Note
                    elif ('make a note' in query) or ('take note' in query):
                        speak("What would you like to write down?")
                        data=takeCommand()
                        from note import Note
                        Note(data)
                        speak("I have a made a note of that.")

                    #Playig random Music
                    elif('play music' in query) or ('play song' in query) or ('music' in query):
                        play_music()

                    #Taking Screenshot Task
                    elif ('take screenshot'in query) or ('take a screenshot'in query):
                        speak("Taking screenshot")
                        import pygame

                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("C:\\Users\\Bhalchandra Khedekar\\Desktop\\MAJOR PROJECT- BEACON\\Screen Shot Sound.mp3")  #replace the path with your screen shot sound.mp3 file
                        pygame.mixer.music.play()
                        from screenshot import takeSS
                        SS = takeSS()
                        speak('Captured screenshot is saved in Screenshots folder.')
                        del SS
                        
                    #Taking Photos
                    elif("photo"in query):
                        from Automation import Camera
                        Camera()
                        speak('Okay sir , The Captured Photo is saved in Photos folder.')
                        

                    #image search
                    elif ('show me images of' in query) or ('images of' in query ) or ('display images' in query):
                        speak("okay sir, check this out")
                        url="https://www.google.com/search?tbm=isch&q="+query[query.find('of')+3:]
                        chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get("chrome").open_new(url)

                    #play game
                    elif "play a game" in query or "game" in query:
                        from game import game_play
                        game_play()

                    #translate words
                    elif "translate" in query or "word" in query:
                        from Translator import translategl
                        translategl()

                    #internetspeed
                    elif "internet speed" in query:
                        wifi = speedtest.Speedtest()
                        upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                        download_net = wifi.download() / 1048576
                        print(f"Wifi Upload Speed is {round(upload_net, 2)} MBps")  # round() function is used to round off the result to 2 decimal places
                        print(f"Wifi Download Speed is {round(download_net, 2)} MBps")
                        speak(f"Wifi Download speed is {round(download_net, 2)} Megabytes per second")
                        speak(f"Wifi Upload speed is {round(upload_net, 2)} Megabytes per second")


                    #schedule your task
                    elif "schedule my day" in query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt","w")
                            file.write(f"")
                            file.close()
                            speak("Enter the number of tasks")
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            speak("Enter the no. of tasks")
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                speak("Write down the task")
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()

                    #Show My Schedule Task
                    elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        speak("Sir chekout notications")
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                        
                    #news speaking
                    elif "news" in query:
                        from NewsRead import latestnews
                        latestnews()
  
                    elif "what do you remember" in query:
                        remember = open("Remember.txt","r")
                        content = remember.read()
                        remember.close()
                        if content:
                            speak("You told me to remember that " + content)
                            remember = open("Remember.txt","w")  # open the file in write mode
                            remember.write("")  # write an empty string to clear the file
                            remember.close()  # close the file after writing
                        else:
                            speak("You haven't told me to remember anything yet.")

                    #rRemember Function
                    elif "remember" in query:
                        from remember import rememberThat
                        rememberThat()

                    #Playing Movies Which are present in your storage
                    elif ("movie" in query):
                        speak("Okay wait a minute, i have to check ,that movie is present in your movies folder or not")
                        from playMovies import play_movie
                        play_movie(query)
                        
                    elif 'i want to hear' in query:
                    #     # Extract the song name from the command
                        song_name = query.split('i want to hear ')[1].split(' song')[0].strip()

                        song_path=''
                        music_dir= "E:\\Playlist Musics"
                        # Search for the song file in the music library folder
                        for root, dirs, files in os.walk(music_dir):
                            for file in files:
                                if file.startswith(song_name) and file.endswith('.mp3'):
                                    song_path = os.path.join(root, file)
                                    break

                        # Use the file explorer to open the music file
                        if song_path:
                            os.startfile(song_path)
                            speak(f"Now playing {song_name}")
                            engine.runAndWait()

                            # If the song file is not found, provide feedback to the user
                        else:
                            speak(f"Sorry, I could not find {song_name} in your music library")
                            engine.runAndWait()

                    
                    # If the user says "pause music"
                    elif 'pause song' in query:
                        # Send the keyboard shortcut to pause the music
                        pyautogui.hotkey('ctrl', 'p')

                    # If the user says "stop music"
                    elif 'resume' in query:
                        # Send the keyboard shortcut to stop the music
                        pyautogui.hotkey('ctrl', 'p')

                    #Youtube Controls like Play, Pause , Mute , Volume up and down 
                    elif "pause video" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play video" in query:
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute video" in query:
                        pyautogui.press("m")
                        speak("video muted")
                    elif "unmute video" in query:
                        pyautogui.press("m")
                        speak("video unmuted")

                    elif "volume up" in query or "volume of" in query:
                        from keyboard1 import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        from keyboard1 import volumedown
                        speak("Turning volume down, sir")
                        volumedown()

                    #Email Sending
                    elif "email to" in query:
                        from sendEmail1 import *
                        recipient_name = extract_recipient_name(query)
                        recipient_email = get_recipient_email(recipient_name)
                        if recipient_email:
                            speak("What should I write in the email?")
                            content = get_email_content()
                            if content != "None":
                                sendEmail(to=recipient_email, content=content)
                            else:
                                print("Sorry, I couldn't get the email content.")
                                speak("Sorry, I couldn't get the email content.")

                    elif 'search' in query:
                        search_query = query.replace('search', '').strip()
                        speak(f"Showing results for {search_query}")
                        pywhatkit.search(search_query)
                        import wikipedia as googleScrap
                        speak("This is what I found on Google.")
                        try:
                            result = googleScrap.summary(search_query, 1)
                            speak(result)
                        except:
                            speak("No speakable output available.")

                    
                    elif ('find location of' in query) or ('show location of'in query):
                        if 'of' in query:
                            speak("Here is the location")
                            url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
                            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
                            webbrowser.get("chrome").open(url)
                                
                    elif ("what is my exact location" in query) or ("What is my location" in query) or ("my current location" in query) or ("exact current location"in query):
                        url = "https://www.google.com/maps/search/Where+am+I+?/"
                        chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get("chrome").open(url)

                        speak("Showing your current location on google maps...")

                    