import sys
import webbrowser
import requests
import speech_recognition as sr
import datetime
import pyttsx3
import pyjokes
import speedtest   
import os
import pywhatkit


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# Whatsapp
def whatsapp(query):
    name = query.replace("send WhatsApp message to ","")

    # if 'me' in name:
    #     speak("What should i type")
    #     msg = takeCommand()
    #     pywhatkit.sendwhatmsg_instantly("+917889118391", msg)
    #     speak("Sending sir!")
        
    if 'karan' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+917696302284", msg)
        speak("Sending sir!")
        
    # elif 'me' in name:
    #     speak("What should i type")
    #     msg = takeCommand()
    #     pywhatkit.sendwhatmsg_instantly("+917889118391", msg)
    #     speak("Sending sir!")
        
    elif 'arsh' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+916283260785", msg)
        speak("Sending sir!")
    
    elif 'harsh' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+916283260785", msg)
        speak("Sending sir!")
    
    elif 'dad' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+917889118391", msg)
        speak("Sending sir!")

    elif 'mum' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+917696302284", msg)
        speak("Sent sir!")
        
    elif 'mom' in name:
        speak("What should i type")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+917696302284", msg)
        speak("Sent sir!")
        
    else:
        print("Give whatsapp command again please")

    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us')
        print(f"User said:- {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    query= query.lower()
    return query

def taskexecution():
    while True:

        query = takeCommand()
        
        if 'wake up' in query:
            speak("I'm ready to take commands sir")

        elif 'exit' in query:
            sys.exit()

        # Always on
        elif 'stop' in query:
            speak(" Okay sir, you can call me anytime, say wake up to give me commands again")
            query = takeCommand()
            while(query != "wake up"):
                query= takeCommand()
                if 'wake up' in query:
                    speak("I'm ready to perform tasks now")
                    taskexecution()
                elif 'exit' in query:
                    sys.exit()
                else:
                    continue

        #Shut Down, Restart
        elif "shutdown" in query:
            speak("Okay sir, I'm ready to work again any time")
            os.system("shutdown /s /t 1") 
        elif "restart" in query:
            speak("okay restarting the system sir")
            os.system("shutdown /r /t 0")
        
        
        #Joke
        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "bad joke" in query:
            speak("Learning from u")
        elif "lame joke" in query:
            speak("Learning from u")
        elif "next joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "one more" in query or "again" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'thanks' in query:
            speak("always available sir")
            
    # Whatsapp
        elif 'whatsapp message' in query:
            whatsapp(query)

    # speed test             NOT WORKING
        elif "Speed test" in query:
            speed_test = speedtest.Speedtest()
            def bytes_to_mb(bytes):
                KB = 1024 # One Kilobyte is 1024 bytes
                MB = KB * 1024 # One MB is 1024 KB
                return int(bytes/MB)

            download_speed = bytes_to_mb(speed_test.download())
            upload_speed = bytes_to_mb(speed_test.upload())
            print("Your Download speed is", download_speed, "MB/S") 
            print("Your upload speed is", upload_speed, "MB/S") 


    #web activities
        elif "location" in query:
            try:
                speak("let me check sir")
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                region = geo_data['region']
                country = geo_data['country']
                speak("you are currently in")
                speak(city)
                speak(region)
                speak(country)
            except:
                speak("check ur network connection please")
        
        #Wikipedia Search
        elif 'search wikipedia for' in query:
            speak('searching Wikipedia')
            query = query.replace("search wikipedia for","")
            webbrowser.open('https://en.wikipedia.org/wiki/'+query)

        #Yputube
        elif 'search youtube for' in query:
            query = query.replace("search youtube for", "")
            speak("searching youtube")
            webbrowser.open('www.youtube.com/results?search_query=' + query)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
        elif "music" in query:
            speak("opening youtube")
            webbrowser.open("https://music.youtube.com")

        #Gmail    
        elif 'gmail' in query:
            speak("opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
        #Google Drive
        elif 'drive' in query:
            speak("opening drive")
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")

        #Google Photos
        elif 'photos' in query:
            speak("opening photos")
            webbrowser.open("https://photos.google.com/")

        #Google Search
        elif 'open Google' in query:
            speak("Opening google")
            webbrowser.open('www.google.com')
            
        elif 'search google for' in query:
            query = query.replace("search google for", "")
            speak("searching google")
            webbrowser.open('www.google.co.in/search?q=' + query)
            
        elif 'open google and search for' in query:
            query = query.replace("open google and search", "")
            speak("searching google")
            webbrowser.open('www.google.co.in/search?q=' + query)

        #instagram
        elif 'open instagram' in query:
            speak("opening insta")
            webbrowser.open("instagram.com")
        
        #Common Tasks            
        elif 'cracked games' in query:
            speak("opening steamunlocked")
            webbrowser.open("steamunlocked.net")
            
        elif 'new Hindi movies' in query:
            speak("opening moviesflix")
            webbrowser.open("https://moviesflix.so/")
            
        elif 'new English movies' in query:
            speak("opening UHDmovies")
            webbrowser.open("https://uhdmovies.click/")

        elif 'torrents' in query:
            speak("opeining torrents site")
            webbrowser.open("1377x.is")
            
    # Local files
        elif "SRS" in query:
            speak("Opening")
            webbrowser.open_new(r'"C:\Study\College\SEM 5\Minor Project\Files-Documents\Project SRS.pdf"')
            
        elif "syllabus" in query:
            speak("Opening")
            webbrowser.open_new(r'C:\\Study\\College\\Syllabus.pdf')
        
        elif "machine learning file" in query:
            speak("Opening")
            webbrowser.open_new(r"C:\\Study\\College\\SEM 6\\ML\\MLLab\\KUNAL ML FILE.docx")
            
        elif "android programming file" in query:
            speak("Opening")
            webbrowser.open_new(r"C:\\Study\\College\\SEM 6\\AP\\AP Lab\\Kunal File.pdf")
    
    
    # Local Folders
        elif "show downloads" in query:
            speak("ok sir")
            dwnPath= "C:\\Users\\ACER\\Downloads"
            os.startfile(dwnPath)
        
        elif "college folder" in query:
            speak("ok sir")
            dwnPath= "C:\\Study\\College"
            os.startfile(dwnPath)

        elif "games folder" in query:
            speak("ok sir")
            dwnPath= "C:\\Users\\ACER\\Desktop\\Games"
            os.startfile(dwnPath)
            
    # Launch apps
        elif 'ms word'in query:
                speak("ok sir")
                codePath= "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codePath)

        elif 'open premiere' in query:
            speak("ok sir")
            proPath= "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2024\\Adobe Premiere Pro.exe"
            os.startfile(proPath)

        elif "photoshop" in query:
            speak("ok sir")
            shopPath= "C:\\Program Files\\Adobe\\Adobe Photoshop 2024\\Photoshop.exe"
            os.startfile(shopPath)

        elif 'open notepad' in query:
            speak("ok sir")
            npdPath= "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npdPath)

        elif 'open edge' in query:
            edgPath= "C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgPath)

        elif 'open o b s' in query:
            speak("opening OBS")
            obsPath= "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obsPath)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<17:
        speak("Good After Noon Sir")
    elif hour>=17 and hour<21:
        speak("good evening sir")
    else:
        speak("u should sleep soon sir")
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f" the time is {strTime}")
    speak("I'm Zehnith. How may i help you")


def mainfunc():
    wishme()
    while True:
        taskexecution()

def exit():
    sys.exit()