import threading
import winspeech

def setInterval(func,time):
    sec = threading.Event()
    while not sec.wait(time):
        func()

def foo():
    winspeech.say_wait("hello adil sir , how are you?")

# using
setInterval(foo,5)