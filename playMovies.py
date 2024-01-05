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
movies_folder = "Your folder address where you have stored a movies"  #need to be edited by yourself

# Initialize the speech recognition engine


# Define a function to play a movie by name
def play_movie(movie_name):
    # Search for the movie file in the movies folder
    movie_file =''
    movie_name =re.sub(r"\b(play|movie)\b", "", movie_name, flags=re.IGNORECASE).strip()
    
    for file in os.listdir(movies_folder):
        if re.match(rf".*{movie_name}.*\.(mp4|mkv|avi)", file, re.IGNORECASE):
            movie_file = os.path.join(movies_folder, file)
            break

    if movie_file:
        os.startfile(movie_file)
        print(f"Now playing: {movie_name} movie")
        speak(f"Now playing: {movie_name} movie)")
    
    else:
        print(f"Sorry, could not find a movie with the name '{movie_name}'")
        speak(f"Sorry, could not find a movie with the name '{movie_name}'.\nHowever, you can watch it on YouTube.")
        pywhatkit.playonyt(movie_name)

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
    

