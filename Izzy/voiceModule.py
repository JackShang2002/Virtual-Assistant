import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
izzy = pyttsx3.init()
voices = izzy.getProperty("voices")
izzy.setProperty("voice", voices[1].id)
izzy.say("Izzy here! What do you need?")
izzy.runAndWait()

try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "izzy" in command:
            print(command)
except:
    pass