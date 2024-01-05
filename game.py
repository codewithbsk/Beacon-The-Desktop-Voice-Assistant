import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def speak_score(Your_Score, My_Score):
    score = "Score: Yours - {} : My - {}".format(Your_Score, My_Score)
    speak(score)
    print(score)

def game_play():
    speak("Let's Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY ROCK PAPER SCISSORS !!")
    i = 0
    Your_Score = 0
    My_Score = 0
    while(i < 5):
        choose = ("rock", "paper", "scissors")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if query == "rock":
            if com_choose == "rock":
                speak("ROCK")
                print("My Choice : ROCK")
                speak_score(Your_Score, My_Score)
            elif com_choose == "paper":
                speak("paper")
                print("My Choice : paper")
                My_Score += 1
                speak_score(Your_Score, My_Score)
            else:
                speak("Scissors")
                print("My Choice : Scissors")
                Your_Score += 1
                speak_score(Your_Score, My_Score)

        elif query == "paper":
            if com_choose == "rock":
                speak("ROCK")
                print("My Choice :ROCK")
                Your_Score += 1
                speak_score(Your_Score, My_Score)
            elif com_choose == "paper":
                speak("paper")
                print("My Choice :paper")
                speak_score(Your_Score, My_Score)
            else:
                speak("Scissors")
                print("My Choice :Scissors")
                My_Score += 1
                speak_score(Your_Score, My_Score)

        elif query == "scissors" or query == "scissor":
            if com_choose == "rock":
                speak("ROCK")
                print("My Choice :ROCK")
                My_Score += 1
                speak_score(Your_Score, My_Score)
            elif com_choose == "paper":
                speak("paper")
                print("My Choice :paper")
                Your_Score += 1
                speak_score(Your_Score, My_Score)
            else:
                speak("Scissors")
                print("My Choice :Scissors")
                speak_score(Your_Score, My_Score)
        i += 1
    
    print(f"FINAL SCORE :- Yours score :- {Your_Score} : My score :- {My_Score}")
    speak(f"FINAL SCORE :- Yours score :- {Your_Score} : My score :- {My_Score}")
    
    if Your_Score > My_Score:
        print("Congratulations! You win!")
        speak("Congratulations! You win!")
    elif Your_Score < My_Score:
        print("Sorry, you lost. Better luck next time!")
        speak("Sorry, you lost. Better luck next time!")
    else:
        print("It's a tie!")
        speak("It's a tie!")