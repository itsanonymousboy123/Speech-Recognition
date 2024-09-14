import pyttsx3 
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()    #with this we will be able to listen

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>3 and hour<10 : speak("Good Morning Sir !")
    elif hour>10 and hour<18 : speak("Good Afternoon Sir !")
    else : speak("Good Evening Sir !")
    
    speak("I am a testing voice assistant developed by Gaurav Please Tell me How may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Try again ...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
   
if __name__ =="__main__":
    wishme()
    while True:
        query = str(takeCommand()).lower()
       
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "give the location of vs code in this "
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("whom to send the email I want email address please provide it")
                to = takeCommand()
                speak("What should I say?")
                content = takeCommand()   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'close'in query or 'stop' in query:
            break
        