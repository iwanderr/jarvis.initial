import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import webbrowser

print("Initializing Jarvis")
 
MASTER = "Aaditya"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function will speak the string
def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning " +MASTER)

    elif hour >=12 and hour <18:
        speak("Good Afternoon " +MASTER)

    else:
        speak("Good Evening " +MASTER)
        
    speak("I am Jarvis. What is that you need helf today")

# this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)        

    try :
        print("recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
            print("hey! say that again please")
            query = None

    return query

# Main Program starts here
speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

# Logic for execution of basic tasks 
if 'wikipedia' in query.lower():
    speak('OK! i will search that on wikipedia for you')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 4)
    print(results)
    speak(results)
    
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.open("google.com")

elif 'open twitter' in query.lower():
    webbrowser.open("twitter.com")

elif 'open flipkart' in query.lower():
    webbrowser.open("flipkart.com")

elif 'open amazon' in query.lower():
    webbrowser.open("amazon.in")


elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\iadit\\Downloads\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'about moment' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\iadit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
