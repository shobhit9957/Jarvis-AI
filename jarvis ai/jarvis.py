import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty("voices")
# print(voice[1].id)
# print(voices )
engine.setProperty('voices', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello, it's me jarvis sir. , how can i help you now!")

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
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.connect("smtp.gmail.com",465)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('shobhitkumarshahi9957@gmail.com', "shobhit9957")
    server.sendmail('shobhitkumarshahi9957@gmail.com', to, content)
    server.quit()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'netflix' in query:
            webbrowser.open("netflix.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'tesla' in query:
            webbrowser.open("tesla.com")
        elif 'music' in query:
            music_dir = 'C:\\Users\\Geetha\\Desktop\\new songs'
            songs = os.listdir(music_dir)
            print(songs)    
            randNumber = random.randint(0,5)
            print(randNumber)
            os.startfile(os.path.join(music_dir, songs[randNumber]))
        elif 'song' in query:
            music_dir = 'C:\\Users\\Geetha\\Desktop\\new songs'
            songs = os.listdir(music_dir)
            print(songs)    
            randNumber = random.randint(0,5)
            print(randNumber)
            os.startfile(os.path.join(music_dir, songs[randNumber]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
        elif 'vs code' in query:
            codePath = "C:\\Users\\Geetha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = 'shobhittiwari9957@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email!")
            speak("Hello, everyone It's me jarvis and I am created by the almighty guy named shobhit, he is an genuine man, he is a hard worker , he always wants action and something going on in life. He gave me the birth, thanks shobhit")
        elif 'quit' in query:
            speak("thanks for having me!")
            exit()
        
