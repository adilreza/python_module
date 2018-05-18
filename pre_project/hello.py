import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("talk somethings")
    audio = r.listen(source)

try:
    #print("You said like : "+ r.recognize_google(audio))
    st = r.recognize_google(audio)
    print("after convertinn string: "+ st)
except:
    pass