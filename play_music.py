import pyttsx3
import os
import random

def play_music():
    music_dir = "E:\\Music" # replace with the actual path to your music folder
    songs = os.listdir(music_dir)
    random.shuffle(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
