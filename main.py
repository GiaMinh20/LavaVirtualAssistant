import os
import webbrowser
import pyautogui #pip install pyautogui
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia    #pip install wikipedia
import pywhatkit #pip install pywhatkit

engine = pyttsx3.init()
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("The current time is ")
    speak(Time)
    print("The current time is ",Time)
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
def lava():
    greeting()
    speak("I am Lava")
    speak("Please tell me how can I help you?")
def takeCMD():
    query = input()
    return query
def takeMic():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="vi-VN")
        print("You: " + query)
    except Exception as e:
        print(e)
        speak("Say again")
        return "None"
    return query
def searchOnWikipedia():
    speak('What are you looking for?')
    print('What are you looking for?')
    query = takeCMD()
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)
    except:
        print("No results were found")

def searchOnGoogle():
    speak('What should I search for?')
    print('What should I search for?')
    search = takeMic()
    webbrowser.open('https://www.google.com/search?q='+search)
def playOnYoutube():
    speak('What should I search on Youtube?')
    print('What should I search on Youtube?')
    search = takeMic()
    pywhatkit.playonyt(search)

def screenshot():
    time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    imageName = f'C:\\Pictures\\{time}.png'
    image=pyautogui.screenshot(imageName)
    image.show()

def openApplication(app):
    if 'garena' in app:
        os.startfile("C:\\Program Files (x86)\\Garena\\Garena\\Garena.exe")
    elif 'word' in app:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif 'excel' in app:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    elif 'vs' in app:
        os.startfile("C:\\Users\\Gia Minh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    else:
        speak("No application found")

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']

def create_note():
    global recognizer
    speak("What do you want to write onto your note?")
    print("What do you want to write onto your note?")
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)
                note = sr.Recognizer().recognize_google(audio, language="vi-VN")
                note = note.lower()
                speak("Choose a filename!")
                print("Choose a filename!")
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)
                filename = sr.Recognizer().recognize_google(audio, language="vi-VN")
                filename = filename.lower()

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done=True
                speak(f"I successfully created the note {filename}")
                print("I successfully created the note " + filename)
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you! Please try again!")
            print("I did not understand you! Please try again!")
def add_note():
    global recognizer
    speak("What todo do you want to add?")
    print("What todo do you want to add?")
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                item = sr.Recognizer().recognize_google(audio, language="vi-VN")
                item = item.lower()

                todo_list.append(item)
                done = True

                speak(f"I added {item} to the to do list!")
                print("I added "+item+" to the to do list!")
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you! Please try again!")
            print("I did not understand you! Please try again!")
def show_todos():
    speak("The items on your to do list are the following")
    for item in todo_list:
        speak(item)
    print(todo_list)
    engine.runAndWait()

if __name__ == '__main__':
    lava()
    while True:
        query = takeMic().lower()
        if 'giờ' in query:
            time()
        elif 'wiki' in query:
           searchOnWikipedia()
        elif 'google' in query:
            searchOnGoogle()
        elif 'youtube' in query:
            playOnYoutube()
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'dạy học số' in query:
            webbrowser.open('https://fhqx.hcmute.edu.vn/')
        elif 'document' in query:
            os.system('explorer C://{}'.format(query.replace('document','')))
        elif 'ứng dụng' in query:
            openApplication(query)
        elif 'chụp màn hình' in query:
            screenshot()
        elif 'tạo' in query:
            create_note()
        elif 'thêm hoạt động' in query:
            add_note()
        elif 'danh sách hoạt động' in query:
            show_todos()
        elif 'thoát' in query:
            speak("Good bye sir!")
            quit()


