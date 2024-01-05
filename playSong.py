import os
import re
import speech_recognition
import pyttsx3
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Set the path to your movies folder
song_folder = "E:\\Playlist Musics"   # replace with the actual path to your music folder

# Initialize the speech recognition engine


# Define a function to play a movie by name
def play_song(song_name):
    # Search for the movie file in the movies folder
    song_file =''
    song_name =re.sub(r"\b(play|song)\b", "", song_name, flags=re.IGNORECASE).strip()
    
    for file in os.listdir(song_folder):
        if re.match(rf".*{song_name}.*\.(mp3|mk4|avi)", file, re.IGNORECASE):
            song_file = os.path.join(song_folder, file)
            break

    if song_file:
        os.startfile(song_file)
        print(f"Now playing: {song_name} song")
        speak(f"Now playing: {song_name} song)")
    
    else:
        print(f"Sorry, could not find a song with the name '{song_name}'")
        speak(f"Sorry, could not find a song with the name '{song_name}'.\nHowever, you can listen it on YouTube.")
        pywhatkit.playonyt(song_name)

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
    

