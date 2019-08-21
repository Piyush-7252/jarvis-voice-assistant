import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pdhodiyal@gmail.com','piyush100')
    server.sendmail('pdhodiyal@gmail.com',to,content)
    server.close()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good after noon")
    else:
        speak("good evening")
    speak(" i am jarvish sir please tell me how may i help you")

def takeCommand():
    # it take microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        r.energy_threshold=400
        audio=r.listen(source)


    try:
        print("recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)

    except Exception as e:
        #print(e)

        print("say that again plz")
        return "None"
    return query


if __name__=="__main__":
    #speak("piyush is a good boy")


    wishMe()

    while True:
        query=takeCommand().lower()

    # logic for executing task based on query
        if 'wikipedia' in query :
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif  "play music" in query:
            music_dir='E:\\favsong'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open vs code' in query:
            codepath="C:\\Users\\smoker\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to piyush' in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to="piyushdhodiyal@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir i am not able to send email")
        elif 'stop' in query:
            break
        




