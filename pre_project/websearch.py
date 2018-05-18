import speech_recognition as sr
import  webbrowser as web
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r=sr.Recognizer()
with sr.Microphone() as source:
    print('say somethings')
    word=r.listen(source)
    print('Ok!! Done')

try:
    test=r.recognize_google(word)
    print("You said:= " +test)
    #final_text='www.google.com/'+test
    final_text='https://www.google.com/search?q='+test
    web.get(chrome_path).open(final_text)
except:
    pass