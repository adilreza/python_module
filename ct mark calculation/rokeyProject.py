import sys
import math
from tkinter import *
student_roll=[]
student_mark=[]
def atmark(percent):
    if(percent>=90):
        return 8
    elif(percent>=85):
        return 7
    elif(percent>=80):
        return 6
    elif (percent >= 70):
        return 5
    elif (percent >= 60):
        return 4
    else:
        return 0

def searching():
    flag=0
    takeroll=src.get()
    l=len(student_roll)
    for i in range(l):
        if(takeroll==student_roll[i]):
            Label(myproject, text="Ohhh!! Foound: %d" % student_mark[i], font=("bold", 20)).place(x=0, y=250)
            flag=1
    if(flag==0):
        Label(myproject, text="Sorry Not Foound:", font=("bold", 20)).place(x=0, y=250)



def calculotion():
    ctf1=ct1.get()
    ctf2=ct2.get()
    ctf3=ct3.get()
    ctf4=ct4.get()
    ctf1=int(ctf1)
    ctf2=int(ctf2)
    ctf3=int(ctf3)
    ctf4=int(ctf4)
    mn=min(ctf1,ctf2)
    mn=min(mn,ctf3)
    mn=min(mn,ctf4)
    rollf=roll.get()
    totalct=ctf1+ctf3+ctf2+ctf4;
    totalct=totalct-mn
    avg=math.ceil(totalct/3)
    #Label(myproject,text=avg).place(x=375,y=450)
    presentingf=presenting.get()
    presentingf=int(presentingf)
    perscentage=math.ceil((presentingf/65)*100)
    attendence_mark=atmark(perscentage)
    Label(myproject, text="Ct Average is: %d"%avg, font=("bold", 20) ).place(x=375,y=450)
    Label(myproject, text="Attendence is: %d"%attendence_mark,font=("bold", 20) ).place(x=375,y=490)
    Label(myproject, text="------------------------------------------------------------------", fg="green").place(x=375,y=530)
    finalmark=avg+attendence_mark
    Label(myproject, text="Total Obtaind: %d" % finalmark, font=("bold", 20)).place(x=375, y=550)
    student_roll.append(rollf)
    student_mark.append(finalmark)


myproject=Tk()

roll=StringVar()
ct1=StringVar()
ct2=StringVar()
ct3=StringVar()
ct4=StringVar()
presenting=StringVar()
src=StringVar()
total=65

myproject.geometry('1080x700')
myproject.title("Hello Welcome To Simple Countings")
header=Label(myproject, text="WELCOME TO STUDENT'S MARKING SYSTEM", fg="red",underline=0,font=("bold",25,"italic"))
header.pack()

labelspace=Label(myproject, text="  ")
labelspace.place(y=30,x=100)
labelspace.pack()

header=Label(myproject, text="Student Roll", fg="green",font=("bold",17,"italic"))
header.pack()
rollt=Entry(myproject,textvariable=roll, width=40).pack()

labelspace=Label(myproject, text="  ")
labelspace.place(y=50,x=100)
labelspace.pack()

cttitle=Label(myproject, text="---- Four Class Test Mark's of This Student ----", fg="green",font=("bold",15,"italic"))
cttitle.pack()

ctt1=Label(myproject, text="#CT1= ",fg='red',font=("italic", 15))
ctt1.place(x=360,y=170)
ctt1val=Entry(myproject,textvariable=ct1, width=10)
ctt1val.place(x=420, y=175)

ctt2=Label(myproject, text="#CT2= ",fg='red',font=("italic", 15))
ctt2.place(x=590,y=170)
ctt2val=Entry(myproject,textvariable=ct2, width=10)
ctt2val.place(x=650, y=175)

ctt3=Label(myproject, text="#CT3= ",fg='red',font=("italic", 15))
ctt3.place(x=360,y=250)
ctt3val=Entry(myproject,textvariable=ct3, width=10)
ctt3val.place(x=420, y=255)


ctt4=Label(myproject, text="#CT4= ",fg='red',font=("italic", 15))
ctt4.place(x=590,y=250)
ctt4val=Entry(myproject,textvariable=ct4, width=10)
ctt4val.place(x=650, y=255)


present2=Label(myproject, text="--- Student Attended Classes ---", fg="green",font=("bold",19,"italic"))
present2.place(x=370, y=300)
present3=Entry(myproject,textvariable=presenting, width=10).place(x=520, y=340)

btn=Button(myproject, text="- CALCULATE NOW -",width=90,bg='blue',fg="white", command=calculotion)
btn.place(x=220, y=390)




ctt1=Label(myproject, text="Roll please.....",fg='blue',font=("italic", 15))
ctt1.place(x=0,y=170)
ctt1val=Entry(myproject,textvariable=src, width=15)
ctt1val.place(x=15, y=195)

btn=Button(myproject, text="-SearcH-",width=20,bg='blue',fg="white", command=searching)
btn.place(x=0, y=220)

mainloop()