import yagmail
import re
import speech_recognition
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 12)

    try:
        print("Processing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Oops... Sorry, I didn't get you. Please check your Internet Connection...")
        # speak("Sorry, I didn't get you.")
        return "None"
    return query

email_list = {
    #add your friends email_address
    'frd1': 'frd1@gmail.com',
    'frd2': 'frd2@gmail.com',
    # Add more names and emails as needed
}

def extract_recipient_name(query):
    recipient_name = re.sub(r"\b(email to|email)\b", "", query, flags=re.IGNORECASE).strip()
    return recipient_name

def sendEmail(to, content, subject="This is an automated email"):
    try:
        yag = yagmail.SMTP('your_email_address', 'your_password') #make sure less secure app acceess in on for your account or google it it.
        yag.send(to=to.lower(), subject=subject, contents=content)
        print("Email has been sent successfully.")
        speak("Email has been sent successfully.")
    except Exception as e:
        print(e)
        print("Sorry, I'm unable to send this email.")
        speak("Sorry, I'm unable to send this email.")

def get_recipient_email(recipient_name):
    if recipient_name.lower() in email_list:
        recipient_email = email_list[recipient_name.lower()]
        return recipient_email
    else:
        print(f"Sorry, I couldn't find the email address for {recipient_name}.")
        speak(f"Sorry, I couldn't find the email address for {recipient_name}. Please write down the email address.") #will take email address of friend which is not in email_list
        recipient_email = input("Enter the Email Address:")
        return recipient_email.lower()



def get_email_content():
    content = takeCommand()
    return content

if __name__ == "__main__":
    while True:
        query = takeCommand()
        if "email to" in query:
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
                    try:
                        content = get_email_content()
                        if content != "None":
                            sendEmail(to=recipient_email, content=content)

                    except Exception as e:
                        print(e)
                        print("Sorry, I'm unable to send this email.")
                        speak("Sorry, I'm unable to send this email.")

takeCommand()