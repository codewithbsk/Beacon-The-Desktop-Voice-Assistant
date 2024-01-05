import os
import re
import speech_recognition
import pyttsx3
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Set the path to your movies folder
movies_folder = "D:\\Movies\\Bollywood movies"  # replace with the actual path to your movies folder

# Initialize the speech recognition engine


# Define a function to play a movie by name
def play_movie(movie_name):
    # Search for the movie file in the movies folder
    movie_file =''
    movie_name =re.sub(r"\b(मूवी |लगाओ)\b", "", movie_name, flags=re.IGNORECASE).strip()
    
    for file in os.listdir(movies_folder):
        if re.match(rf".*{movie_name}.*\.(mp4|mkv|avi)", file, re.IGNORECASE):
            movie_file = os.path.join(movies_folder, file)
            break

    if movie_file:
        os.startfile(movie_file)
        print(f"अभी प्लेय हो रही है: {movie_name} movie")
        speak(f"अभी प्लेय हो रही है: {movie_name} movie)")
    
    else:
        print(f"क्षमा करें, इस नाम की कोई फ़िल्म नहीं मिली'{movie_name}'")
        speak(f"Sक्षमा करें, इस नाम की कोई फ़िल्म नहीं मिली'{movie_name}'.\nहालाँकि, आप इसे YouTube पर देख सकते हैं।")
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
    

