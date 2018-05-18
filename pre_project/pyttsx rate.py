import pyttsx3
import winspeech
engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', rate+20)
engine.say("Hello  madam, I am at your services, How can I help you, madam?")
engine.runAndWait()
winspeech.say_wait("Hello sir , I am at your services, Ho can I help you, sir?")