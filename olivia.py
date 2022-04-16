import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def take_command():
    talk('how may i help you')

    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source, timeout=1, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'olivia' in command:
                command = command.replace('olivia', '')
                print(command)
    except:
        pass
    return command


def run_olivia():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'about' in command:
        person = command.replace('about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open notepad' in command:
        talk('opening notepad')
        notepad = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(notepad)
    elif 'close notepad' in command:
        talk('closing notepad')
        os.system('taskkill /f /im notepad.exe')

    elif 'open browser' in command:
        browser = 'C:\\Program Files\\Google\\Chrome\\Application\\crome.exe'
        os.startfile(browser)
    elif 'close browser' in command:
        talk('closing browser')
        os.system('taskkill /f /im crome.exe')
    else:
        talk('Please say the command again.')


while True:
    run_olivia()
