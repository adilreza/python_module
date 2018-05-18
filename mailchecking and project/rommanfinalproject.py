import sys
import math
import os
import webbrowser

from tkinter import *
import pyttsx3
import winspeech
import pyaudio
import speech_recognition as sr
import bs4 as bs
import urllib.request
engine = pyttsx3.init()


def receive_command():
    reinstance=sr.Recognizer()
    with sr.Microphone() as source:
        audio=reinstance.listen(source)
        try:
            st = reinstance.recognize_google(audio)
            return st;
        except:
            pass
    return 0;

def readit(result):
    engine.say(result)
    engine.runAndWait()
    engine.say("Do YOu want To search another things?")
    engine.runAndWait()
    st=receive_command()
    if(st=="yes"):
        print(st)
        FAQ()
    else:
        pass
    return 0



def websearchingfinal(search):
    mainurl = "https://en.wikipedia.org/wiki/"
    finalurl = mainurl + search
    urlores = urllib.request.urlopen(finalurl)
    allhtmlresult = bs.BeautifulSoup(urlores, 'html.parser')
    firstp = allhtmlresult.p
    textresult = firstp.text
    engine.say("After Searchin from google the result is...")
    print(textresult)
    readit(textresult)
    return  0;

def common_repaying(command):
    st="Command accepted, Sir. YOu Wanted To search about.."
    finalst=st+command
    engine.say(finalst)
    engine.runAndWait()
    engine.say("Is it Right Sir?")
    engine.runAndWait()
    flag=receive_command()
    if(flag=="yes"):
        print(flag)
        engine.say("Ok I am searching in google about,"+command)
        websearchingfinal(command)
    else:
        print("Answer dennayed")
        websearching()
    return 0;

def websearching():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 20)
    engine.say("Wow!! Your have choosen Web searching.")
    engine.say("What do You want To search?")
    engine.runAndWait()
    st=receive_command()
    common_repaying(st)
    return 0;


def FAQ():
    engine.say("Please, Say something I am waiting For You, sir.")
    engine.runAndWait()
    st=receive_command()
    print(st)
    common_repaying(st)
    return 0;



def welcome():
    engine.say("Helllo, This is Your Personal Assistant. I am here to help you??")
    engine.say("I can Perform, below describing all of this.")
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate-20)
    engine.say("Listen CArefully.")
    engine.say("1... Quick Web ,searching..")
    engine.say("2... Quick web ,Scrapping.")
    engine.say("3... Text reading.")
    engine.say("4... Computer maintainging by voice.")
    engine.runAndWait()
    engine.setProperty('rate', rate-10)
    engine.say("If You Want To add more feature programme my module, thank you")
    engine.say("Now time to enjoying it.")
    engine.runAndWait()
    return 0



def webresultfromwiki(search):
    mainurl="https://en.wikipedia.org/wiki/"
    finalurl=mainurl+search
    urlores=urllib.request.urlopen(finalurl)
    allhtmlresult=bs.BeautifulSoup(urlores, 'html.parser')
    firstp=allhtmlresult.p
    textresult=firstp.text
    return textresult

def readgiven(rcv):
    engine.say(rcv)
    engine.runAndWait()

def spstop():
    engine.stop()
def websearhhere():
    common="You wanted To search about, "
    common2="Please, write something,"
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate-20)
    fcontent=content.get()
    ffcontent=fcontent
    if(fcontent==""):
        engine.say(common2)
        engine.runAndWait()
        return 0
    else:
        fcontent=common+fcontent
        engine.say(fcontent)
        engine.runAndWait()
        engine.say("I am searching in google. just a second")
        engine.runAndWait()
        result=webresultfromwiki(ffcontent)
        if(result!=""):
            T=Text(myproject,height=10,width=100,fg="green",font=("bold",12,"italic"))
            T.place(y=350,x=180)
            T.insert(END, result)
            engine.say("Ok, Found YOur result, listen.")
            readgiven(result)
            return 0
        else:
            engine.say("Sorry, Not found , check your keywords again.")
            engine.runAndWait()
            return 0

myproject=Tk()

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
content=StringVar()

myproject.geometry('1370x768')
myproject.title("WelCome To mY Little Intelligent System")
btn=Button(myproject, text="-Start-", width="10", command=welcome).pack()

header=Label(myproject, text="WElCOME SIR I AM AT YOUR SERVICES", fg="black",underline=0,font=("bold",25,"italic"))
header.pack()

headerspace=Label(myproject, text="................................................", fg="red", font=("italic", 30) )
headerspace.pack()

header2=Label(myproject, text="Enter The Specific Keywords..", fg="green", underline=3,font=("bold",20))
header2.pack()
ctt3val=Entry(myproject,textvariable=content, width=60,font=("bold", 16))
ctt3val.pack()


btn=Button(myproject, text="-Search Here-",width=20,bg='blue',fg="white", font=("bold",12), command=websearhhere)
btn.place(x=400, y=195)
btn2=Button(myproject, text="-SearcH Browser-",width=20,bg='blue',fg="white", font=("bold",12), command=spstop)
btn2.place(x=600,y=195)

btn2=Button(myproject, text="-voice search-",width=20,bg='red',fg="white", font=("bold",12),command=FAQ)
btn2.place(x=800,y=195)

mainloop()




