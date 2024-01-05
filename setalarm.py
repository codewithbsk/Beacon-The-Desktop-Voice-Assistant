import pyttsx3
import datetime
import time
import re
import os

engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to set an alarm for a given time
def set_alarm(hour, minute):
    now = datetime.datetime.now()
    alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # Check if alarm time is in the past
    if alarm_time < now:
        alarm_time += datetime.timedelta(days=1)

    alarm_time_str = alarm_time.strftime('%I:%M %p')
    print(f"Alarm set for {alarm_time_str}")
    speak(f"Alarm set for {alarm_time_str}")

    # Wait until alarm time
    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print("Wake up!")
            speak("Wake up!")
            os.startfile("C:\\Users\\Bhalchandra Khedekar\\Desktop\\MAJOR PROJECT- BEACON\\Alarm.mp3") # replace with the actual path to your Alarm.mp3 file
            break
        time.sleep(10) # Wait 1 minute before checking the time again


# import datetime
# import threading
# import time
# import os
# import pyttsx3
# from playalarm import play_alarm

# engine = pyttsx3.init()


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # def play_alarm():
# #     print("Wake up!")
# #     speak("Wake up")
# #     os.startfile("C:\\Users\\Bhalchandra Khedekar\\Desktop\\MAJOR PROJECT- BEACON\\Alarm.mp3")

# def set_alarm(hour, minute):
#     now = datetime.datetime.now()
#     alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

#     # Check if alarm time is in the past
#     if alarm_time < now:
#         alarm_time += datetime.timedelta(days=1)

#     alarm_time_str = alarm_time.strftime('%I:%M %p')
#     print(f"Alarm set for {alarm_time_str}")
#     speak(f"Alarm set for {alarm_time_str}")


#     while True:
#         now = datetime.datetime.now()
#         if now >= alarm_time:
#             # Start a new thread to run the alarm
#             alarm_thread = threading.Thread(target=play_alarm)
#             alarm_thread.start()
#             break
#         time.sleep(60)




