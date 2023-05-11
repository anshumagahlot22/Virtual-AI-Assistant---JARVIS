import webbrowser
import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from twilio.rest import Client

listener=aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction=instruction.lower()
            if "jarvis" in instruction:
                instruction=instruction.replace('jarvis'," ")
                print(instruction)
            
    except:
        pass
    return instruction
 
def play_Jarvis():

    instruction=input_instruction()
    print(instruction)
    if "play" in instruction:
        song=instruction.replace('play',"")
        talk("playling" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        print('Current time' + time)
        talk('Current time' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        print("Today's date " + date)
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        print('I am fine, how about you')
        talk('I am fine, how about you')
    
    elif 'what is your name' in instruction:
        print('I am Jarvis, What can I do for you?')
        talk('I am Jarvis, What can I do for you?')
    
    elif 'who is' in instruction:
        human = instruction.replace('who is ',"")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    elif "open google" in instruction:
        talk("Opening Google ")
        webbrowser.open("www.google.com")

    elif 'joke' in instruction:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
 
    elif 'bye' in instruction:
        print('See you later')
        talk('See you later')
    else:
        print('Please Repeat')
        talk('Please Repeat')

play_Jarvis()