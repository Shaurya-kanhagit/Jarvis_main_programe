# from curses.ascii import alt
from multiprocessing.spawn import prepare
import os
from firebase import firebase
import random
# from ast import Try
from cmath import e
from email.mime import audio
from traceback import print_tb
from turtle import forward
import pyttsx3
import playsound
import wikipedia
import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import keyboard
from keyboard import press_and_release



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
s = 0
def wish_2():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:    
        print('Good afternoon sir ')     
        speak('Good afternoon sir ')     
    elif hour>=12 and hour<18:
        print('Good afternoon sir ')     
        speak('Good afternoon sir ')  
    else:
        print('Good afternoon sir ')     
        speak('Good afternoon sir ') 
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Jarvis:- Good morning sir kanha")    
        speak('Good morning sir kanha')    
    elif hour>=12 and hour<18:
        print("Jarvis:- Good afternoon sir kanha")
        speak("Good afternoon sir kanha")
    else:
        print("Jarvis:- Good evening sir kanha")
        speak("Good  evening sir kanha")
    speak('how may i help you')
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'Kanha:- {query}\n')

    except Exception as e:
       print('say that again please ')
       return "None"
    return query
if __name__== "__main__":
    wish_me()
    while True:

#music 
        songs123 = [0,1,2,3,4,5]
        a10 = random.choice(songs123)
        a11 = a10 +1
# a11 = random.choice(songs123) 
        ###
        query= takecommand().lower()
        print(query)
        if 'wikipedia' in query:
            speak('searching in wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
###software operations###    
        elif 'open github' in query:
            print("Opening your github account here:-")
            speak("Opening your github account here:-")
            webbrowser.open('https://github.com/')
        elif 'what all i dream' in query:
            print('IIT delhi computer science branch')
            print('Apple macbook air')
            print('BMW X5 ')
            print('BMW 330 li ')
            speak('IIT delhi computer science branch')
            speak('BMW X5 ')
            speak('BMW 330 li ')
            speak('Apple macbook air')


        elif 'youtube' in query:
            print("Opening youtube")
            speak("Opening youtube")
            webbrowser.open('https://www.youtube.com/')
        elif 'open thunderbird' in query:
            print("Lauching thunderbird")
            speak("Lauching thunderbird")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Thunderbird.lnk")
        elif 'close thunder' in query:
            print("closing thunderbird")
            speak("closing thunderbird")
            press_and_release('alt+f4')
        elif 'open whatsapp' in query:
            print('launching whatsapp on your system')
            speak('launching whatsapp on your system')
            os.startfile("C:\\Users\\shaur\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk")
        elif 'teams' in query:
            print('Launching teams')
            speak('Launching teams')
            os.startfile("C:\\Users\\shaur\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk")
        elif 'Open brave' in query:
            print("Lauching brave")
            speak("Lauching brave")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk")
        elif 'open steam' in query:
            print("Lauching steam ")
            speak("Lauching steam ")
            os.startfile("C:\\Users\\shaur\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk")
        elif 'show chrome' in query:
            print('showing chrome on windows')
            speak('showing chrome on windows')
            press_and_release('win+1')
        elif 'show chrome' in query:
            print('showing explorer on windows')
            speak('showing explorer on windows')
            press_and_release('window+')
        elif 'premier pro' in query:
            print("Okay sir launching premier pro")
            speak("Okay sir launching premier pro")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Premiere Pro 2020.lnk")
        elif 'open zoom' in query:
            print("Opening zoom")
            speak("Opening zoom")
            os.startfile("C:\\Users\\shaur\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk")
###
###music###
        elif 'music' in query:
            music_dir = 'C:\\Users\\shaur\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            print('Playing songs ')
            speak('Playing songs ')
            s =+1
            os.startfile(os.path.join(music_dir,songs[a10]))
        elif 'change song' in query:
                music_dir = 'C:\\Users\\shaur\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                print(' Changing song ')
                speak(' Changing song ')
                os.startfile(os.path.join(music_dir,songs[a11]))
        elif 'jo bheji thi dua' in query:
            print("Playing bheji thi dua")
            speak("Playing bheji thi dua")
            webbrowser.open('https://www.youtube.com/watch?v=DB0XGQRPIqo&list=RDDB0XGQRPIqo&start_radio=1')
###
        
###sleep mode###
        elif 'sleep mode' in query:
            print('Okay sir going in sleep mode')
            speak('Okay sir going in sleep mode')
            speak(wish_2)
            exit()
###
###time###
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print('sir its',strTime)
            speak(f'sir its {strTime}')
        elif 'Okay' in query:
            print("Anything else sir")
            speak("Anything else sir")
###
###extra###
        elif 'hey jarvis' in query:
            print('Hello Sir kanha i am always here ')
            speak('Hello Sir kanha i am always here ')
#chrome auto mation###
        elif 'close tab' in query:
            print("Opening tab")
            speak("Opening tab")
            press_and_release('ctrl+w')
        elif 'open history' in query:
            print("Opening tab")
            speak("Opening tab")
            press_and_release('ctrl+h')
        elif 'open downloads' in query:
            print("Opening tab")
            speak("Opening tab")
            press_and_release('ctrl+j')
        elif 'new window' in query:
            print("Opening tab")
            speak("Opening tab")
            press_and_release('ctrl+n') 
        elif 'full screen' in query:
            print('doing full screen')
            speak('doing full screen')
            press_and_release('f11')
        elif 'chrome option' in query:
            print('Opening chrome options')
            speak('Opening chrome options')
            press_and_release('alt+f')
###
#YOUTUBE AUTOMATION###
        elif  'forward' in query:
            print("forwarding 10 sec")
            speak('forwarding')
            press_and_release('l')
        elif 'second' in query:
            print("forwarding 10 sec")
            speak('rewinding')
            press_and_release('k')  
        elif 'pause' in query:
            print("Pausing the video")
            speak("Pausing the video")
            press_and_release('space')
###else###
        else:
            #pehele query print kara and then make an entry in my sql database basixally query koo database mai add karva dee
            print("Jarvis :- I am still learning please try with this same query after sometime")
            print('inputing this query in Database {-----}')
            
            firebase = firebase.FirebaseApplication("https://jarvis-797d8-default-rtdb.firebaseio.com/",None)
            data = {
                'question':query
            }
            result = firebase.post('/jarvis-797d8-default-rtdb/Main_question',data)
            # speak("I am still learning please try with this same query after sometime")
###
