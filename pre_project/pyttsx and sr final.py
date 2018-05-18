import speech_recognition as sr
import  pyttsx3
import pyaudio
# Record Audio

engine=pyttsx3.init()

said=""
r = sr.Recognizer()

def testing(rcv):
    if rcv=="how are you":
        engine.say("I am fine sir. HOw can I help you")
    elif rcv=="hi":
        engine.say("Hello, sir, How are you?")
    else:
        engine.say(rcv)

    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)

    engine.runAndWait()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    said=r.recognize_google(audio,language="en-us")
    testing(said)

    print("Speech was: " + r.recognize_google(audio, language = "en-us",show_all=False))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
