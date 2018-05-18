import pyttsx3
import bs4 as bs
import urllib.request
import sys
import winspeech
import speech_recognition as sr
engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', rate-20)

def wecome():
    winspeech.say_wait("WellCome mad, I am Your personar assistant. How can I help you madam")
    return 0
def webresult(search):
    mainurl="https://en.wikipedia.org/wiki/"
    finalurl=mainurl+search
    urlores=urllib.request.urlopen(finalurl)
    allhtmlresult=bs.BeautifulSoup(urlores, 'html.parser')
    firstp=allhtmlresult.p
    textresult=firstp.text
    return textresult

res=input("Enter a text")
getresult=webresult(res)
engine.say(getresult)
engine.runAndWait()
print(getresult)
