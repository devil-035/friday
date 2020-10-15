import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
from pygame import mixer 
import webbrowser
import os
import sys
from pynput.keyboard import Key , Controller
import smtplib
import wolframalpha
from PyQt5 import QtWidgets
import threading
from googletrans import Translator
from PIL import Image
import pyautogui
from colored import fg, attr
from facematch import FACE
app = QtWidgets.QApplication(sys.argv)
facematch=FACE()
facematch.start()
app.exit(app.exec_())
import time
import pynput
import clipboard
import json
from playsound import playsound
import ssl
import certifi
import random
import bs4 as bs
import urllib.request
import requests
from gtts import gTTS
from bs4 import BeautifulSoup
import ctypes
import subprocess as sp
from googlesearch import search
from pynput.keyboard import Key, Controller


reset = attr('reset') # Resets the Text Color to Default.
red = fg('red')       # Prints Text With Red Color.
blue = fg('blue')     # Prints Text With Blue Color.
green = fg('green')   # Prints Text With Green Color.
yellow = fg('yellow') # Prints Text With Yellow Color.


keyboard = Controller()
#playsound("Loading.mp3")
    
ctypes.windll.user32.SystemParametersInfoW(20, 0, "ajj.jpg" , 0) 

codepath = "C:\\Program Files\\Rainmeter\\Rainmeter.exe"
os.startfile(codepath)
time.sleep(2)


class person: 
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

mp3_thanktou_list = ['mp3/friday/thankyou_1.mp3', 'mp3/friday/thankyou_2.mp3']
mp3_listening_problem_list = ['mp3/friday/listening_problem_1.mp3', 'mp3/friday/listening_problem_2.mp3']
mp3_struggling_list = ['mp3/friday/struggling_1.mp3']
mp3_google_search = ['mp3/friday/google_search_1.mp3', 'mp3/friday/google_search_2.mp3']
mp3_greeting_list = ['mp3/friday/greeting_accept.mp3', 'mp3/friday/greeting_accept_2.mp3']
mp3_open_launch_list = ['mp3/friday/open_1.mp3', 'mp3/friday/open_3.mp3', 'mp3/friday/open_2.mp3']
mp3_search_list = ['mp3/friday/seach_found.mp3','mp3/friday/search_1.mp3']
def speak(audio):

    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('rate',170)
for voice in voices:
    engine.setProperty('volume',1)
    engine.setProperty('voice',voices[1].id)


person_obj = person()
asis_obj = asis()
asis_obj.name = 'FRIDAY'
person_obj.name = "ANKIT DHIMAN"


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
        print(red+ "Good Morning Sir..\n" + reset)

    elif hour>=12 and hour<18:
        speak("Good Afternoon  sir ..\n")   
        print(red + "Good Afternoon  sir ..\n" + reset)   

    else:
        speak("good evening sir..\n")  
        print(red + "Good evening sir" + reset)

    playsound('mp3/friday/greeting.mp3')      
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)
      

def takeCommand(ask=""):
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(reset + '\n^\n' + blue + "\n  Listening...\n" + reset)
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print(green + "  Recognizing...\n" + reset)    
        query = r.recognize_google(audio, language='en')
        
        print(green + f"BOSS: {red}> {blue}  {query}\n" + reset)

    


    except Exception as e:
        print(e)    
        print( red + "Say that again please...\n" + reset)  
        return "None"
        
    return query
def shutdown():
    speak(red + 'Are You Sure?' + reset)
    time.sleep(1)
    reply = takeCommand()
    if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply or 'do it' in reply:
        print(yellow + '\n\tShutting Down!.' + reset)
        speak('Ok! Shutting Down the system  in a Minute.')
        os.system('shutdown -s')
        exit()

    else:
        speak('no problem sir !')


if __name__ == "__main__": 
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            play_sound(mp3_search_list)
            try:
                speak('Searching ON Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                play_sound(mp3_google_search) 
                print(green + results)
                speak(results)
                time.sleep(1)

            except:
                print(red + '\n\tUnable to Get Results!' + reset)
                speak("unable to get results")

        elif 'on youtube' in query:
            play_sound(mp3_open_launch_list)
            search_term = query.split("for")[-1]
            search_term = search_term.replace("on youtube","").replace("search","")
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            play_sound(mp3_google_search)
            print(green + f'/nSearching for "{search_term}"' + reset )
            speak("Here is what I found for " + search_term + "on youtube")

        elif 'how are you' in query:
            spea= 'i am fine sir' , 'i am feeling well , sir'
            print(yellow +'\n\t"thanks for asking sir"'+ reset)
            speak(random.choice(spea))
            time.sleep(1)
            continue

        elif'who is your boss' in query:
            print(yellow+'\nANKIT DHIMAN' )
            speak('ankit dhiman is my boss')
            time.sleep(1)
            continue

        elif 'task list' in query or 'tasklist' in query:
            print(green + '\n\tShowing All Running Tasks!' + yellow)
            speak('Showing All Running Tasks!')
            sp.call('tasklist')
        
        elif 'search for' in query and 'youtube' not in query:
            playsound("mp3/friday/search_1.mp3")
            search_term = query.split("for")[-1]
            search_term = search_term.replace("on Google","").replace("search","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            play_sound(mp3_google_search)
            print(green + f'/nSearching for "{search_term}"' + reset )
            speak("Here is what I found for" + search_term + "on google")
            time.sleep(1)

        elif 'calculator' in query:
            play_sound(mp3_open_launch_list)
            calc = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calc)

        elif 'take screen shot ' in query or 'screenshot' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('D:/screen.png')

        elif 'i love you' in query:
            ap = query.replace('i love you','')
            speak("it's hard to understand sir")
            print(red +"\n it's hard to understand" + reset)

        elif 'date' in query or "today's date" in query:
            strDate =datetime.datetime.now().strftime("%m/%d/%y")
            print(blue+  f'\n\t"today is {strDate}"')
            speak(f"today is {strDate}")

        elif ' editior mode' in query:
            print(yellow + 'ok sir '+ reset)
            play_sound(mp3_open_launch_list)
            from LOADING import ls

        elif 'open google' in query:
            play_sound(mp3_open_launch_list)
            webbrowser.open("google.com")
            play_sound(mp3_google_search)
            continue

        elif 'open facebook' in query:
            play_sound(mp3_open_launch_list)
            webbrowser.open("facebook.com")
            continue

        elif 'select all' in query:
            speak('ok sir')
            time.sleep(3)
            with keyboard.pressed(Key.ctrl):
                keyboard.press('a')
                keyboard.release('a')
                speak('done sir')

        elif 'copy' in query:
            speak('ok sir')
            time.sleep(3)
            with keyboard.pressed(Key.ctrl):
                keyboard.press('c')
                keyboard.release('c')
                speak('done sir')

        elif 'paste' in query:
            speak('ok sir')
            time.sleep(3)
            with keyboard.pressed(Key.ctrl):
                keyboard.press('v')
                keyboard.release('v')
                speak('done sir')

        elif 'copy me what i say' in query or 'copy me' in query or 'speak' in query:
            time.sleep(1)
            copu = query.replace("speak","")
            speak(copu)
            time.sleep(1)
            continue

        elif 'launch' in query or 'open' in query:
            query = query.replace('launch ', "")
            query = query.replace('open', "launch")
            app = query.title()
            try:
                os.startfile(app)
                print(yellow+'\n\tLaunching ' + app.title() ) 
                speak(f'Launching {app}!') 
                time.sleep(1)

            except:
                print(red + f"\n\tCouldn't Launch {app.title()}"+ reset)
                speak(f"Couldn't Launch {app}")
                time.sleep(1)
        elif 'clear' in query or 'clean' in query:
            os.system('cls')
            speak('Current Console Cleared')

        elif 'shutdown' in query or 'power off' in query:
            shutdown()

        elif 'how are you' in query:
            spea= 'i am fine sir' , 'i am feeling well , sir','feeling great sir'
            speak(random.choice(spea))
            continue

        elif 'thank you' in query or 'thanks' in query or 'thanks friday' in query or 'thank you friday' in query:
            play_sound(mp3_thanktou_list)

        elif 'jarvis' in query or 'hello jarvis' in query:
            speak('sir my name is friday ,not jarvis so please call me hello friday again')

        elif 'hello' in query or 'hi' in query or 'hello friday' in query:
            print( yellow +"\n\tHELLO SIR! HOW CAN I HELP YOU")
            speak(' hello sir ,how can i help you')
             

        elif 'search' in query or 'search about' in query:
            play_sound(mp3_search_list)
            results = wikipedia.summary(query, sentences=1)
            play_sound(mp3_google_search)
            print(green + results)
            speak(results)

        elif "calculate" in query or 'add' in query or 'subtract' in query or 'multiplie' in query or 'divide' in query or 'plus' in query or 'minus ' in query:
            play_sound(mp3_google_search)
            client = wolframalpha.Client("R2K75H-7ELALHR35X")
            query = query.replace("calculate", "")
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(red  + "\n\tcalculating.."+ reset)
            speak("calculating..")
            time.sleep(0.5)
            print(green + f"\n\tThe answer is {answer}"+ reset) 
            speak(f"The answer is {answer}")
              
        elif "Good Morning" in query or 'good afternoon' in query or 'good evening' in query:
            speak("A warm" + query) 
            speak("How are you") 
            speak(person_obj.name)

        elif 'open stackoverflow' in query:
            play_sound(mp3_google_search)
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query or 'play song' in query:
            play_sound(mp3_open_launch_list)
            path = "C:/Users/joras/Music/"
            ANK = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
            AC = random.choice(ANK)
            mixer.init()
            mixer.music.load(AC) 
            print(green + '\n\tPlaying Music! ' + reset)
            mixer.music.play()
            time.sleep(2)

        elif 'stop music' in query or 'stop song ' in query or 'band karo' in query or 'flag' in query:
            mixer.music.stop()
            print(green + '\n\t Music stoped! ' + reset)
            

        elif 'pause music' in query:
            speak('ok sir')
            mixer.music.pause()

        elif 'resume song' in query or 'start music' in query or 'start song' in query:
            speak('ok sir')
            mixer.music.resume()
            

        elif 'the time' in query:
            playsound('mp3/friday/open_1.mp3')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'weather' in query:
            play_sound(mp3_open_launch_list)
            speak('searching on your location')
            from WETHERLOADING import WH
            search= query.replace("search","")
            URL=f"https://www.google.com/search?q={search}"
            req =requests.get(URL)
            sav = BeautifulSoup(req.text,"html.parser")
            update = sav.find("div",class_ = "BNeawe").text
            speak(f"Sir, the tempreature on your location is  {update}")
            print(f"Sir, the tempreature on your location is  {update}")


        elif'who is your boss' in query:
            speak('Ankit dhiman is my boss')
            print('ANKIT DHIMAN' )
            continue

        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('friday.txt', 'w') 
            speak("Sir, Should i include date and time") 
            time.sleep(2)
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show me your written file" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(green + "ok sir" + reset) 
            speak(file.read(6)) 
        
        elif "don't listen" in query or "stop listening" in query: 
            print( red + "for how much time you want to stop jarvis from listening commands"+ reset)
            speak("for how much time you want to stop jarvis from listening commands") 
            a = takeCommand()
            time.sleep(a) 
            print(a) 

         
   
        elif 'exit' in query or 'go offline'in query or 'goodbye' in query or 'goodbye friday' in query:
            playsound('mp3/friday/bye.mp3')        
            exit()

        elif 'what is my location' in query or 'my location' in query:
            Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
            loc = Ip_info['region']
            speak(f"You must be somewhere in {loc}")
            continue

        elif 'what is your name' in query:
            speak(f"my name is {asis_obj.name}")
            time.sleep(1)
            continue

        elif 'chnange my name to' in query:
            person_name = query.split("to")[-1].strip()
            speak("okay, i will remember that " + person_name)
            person_obj.setName(person_name)
            time.sleep(1)

        elif 'what is my name' in query:
            speak("Your name must be " + person_obj.name)
        
            continue

        elif "who are you" in query or "define yourself" in query: 
            speaks = '''Hello, I am friday, Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            speak(speaks) 
            continue
        

        elif "who made you" in query or "created you" in query: 
            speaks = "I have been created by ANKIT DHIMAN."
            print(speaks)
            speak(speaks) 
            continue
        elif "capture" in query or 'my screen' in query or 'screenshot' in query:
            play_sound(mp3_open_launch_list)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('D:/games/screen.png')
            speak('done boss')

        elif 'change wallpaper' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\\main\\akk.jpg', 0)
            speak("wallpaper changed sir")

        elif 'another wallpaper' in query:
            speak("ok sir")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\\raain\\qw.JPG', 0)
            speak("wallpaper changed boss")
            
        
        elif 'definition of' in query:
            definition = takeCommand("what do you need the definition of")
            url=urllib.request.urlopen('https://en.wikipedia.org/wiki/' +definition)
            soup=bs.BeautifulSoup(url,'lxml')
            definitions=[]

            for paragraph in soup.find_all('p'):
                definitions.append(str(paragraph.text))
            if definitions:
                if definitions[0]:
                    
                    print( red + 'i m sorry i could not find that definition, please try a web search'+ reset )
                    speak('i m sorry i could not find that definition, please try a web search')
                elif definitions[1]:

                    print(green+ 'here is what i found '+definitions[1] + reset )
                    speak('here is what i found '+definitions[1])
                else:

                    print(green+ 'here is what i found '+definitions[2] + reset )
                    speak ('Here is what i found '+definitions[2])    
            else:
        
                speak("i am sorry i could not find the definition of ")

        elif 'what' in query or 'how' in query or 'when ' in query or 'who' in query or 'where' in query:

            try:
                query = query.replace('what','')
                query = query.replace('how','')
                query = query.replace('when','')
                query = query.replace('who','')
                query = query.replace('where','') 
                query = query.replace('when','')
                results = wikipedia.summary(query, sentences=2)
                play_sound(mp3_google_search)
                print(green +  results)
                speak(results)
            except:
                print(red+ "\n\t  SORRY SIR ! I CAN NOT ABLE TO FIND ABOUT THIS" + reset)    
                speak("SORRY SIR ! I CAN NOT ABLE TO FIND ABOUT THIS")
        
