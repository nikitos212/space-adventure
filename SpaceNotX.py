from tkinter import *
from PIL import ImageTk,Image,ImageOps
import smtplib
k=0
shots=0
text=30
def def2():
    newtop=Toplevel()
    newtop.title("Отзыв")
    newtop.geometry("350x250")
    newtop.geometry("+{}+{}".format(546, 312))
    newtop.resizable(False, False)
    luub=Text(newtop,font=28,width=35,height=10)
    buut=Button(newtop,text="Отправить")
    buut.bind("<Button-1>",com)
    luub.pack()
    buut.pack()
    newtop.mainloop()
def com(event):
    new2top=Toplevel()
    new2top.title("Спасибо за Ваш отзыв!")
    new2top.geometry("350x250")
    new2top.geometry("+{}+{}".format(546, 312))
    new2top.resizable(False, False)
    img111=ImageTk.PhotoImage(Image.open("thanks.jpg"))
    labyl=Label(new2top,image=img111)
    str3="Спасибо, ещё один одинокий"+"\n"+" разработчик стал немного счастливее!"
    lubk=Label(new2top,text=str3,font=30)
    lubk.pack()
    labyl.pack()
    new2top.mainloop()
def def1():
    global shots
    global score
    global top
    shots=0
    score=0
    lab101["text"]=str(score)+"/5"
    lab201["text"]=str(shots)+"/7"
    if top!=None:
        top.destroy()
def startofgame():
    topchik=Toplevel()
    topchik.title("Полезный совет")
    topchik.geometry("350x90")
    topchik.geometry("+{}+{}".format(846, 312))
    topchik.resizable(False, False)
    str1="Рекомендуем, сначала прочитать правила"+"\n"+"(открытие - клик левой кнопкой мыши)."+"\n"+"Удачи!"
    lub=Label(topchik,bg="gold",text=str1,font=40)
    lub.pack()
    topchik.mainloop()
def function(event):
    top1=Toplevel()
    top1.title("Правила")
    top1.geometry("450x150")
    top1.geometry("+{}+{}".format(370, 250))
    top1.resizable(False, False)
    str2="Правила."+"\n"+"Главная задача - попасть в двигающуюся панель 5 раз,"+"\n"+"кол-во попаданий отображается в блоке (score),"+"\n"+"но при этом учитывается количество выстрелов,"+"\n"+"для победы не более 7, оно отображается в блоке (shots)."+"\n"+"Слишком часто делать выстрелы не рукомендуется."+"\n"+"Игра идёт без времени :) ."
    labelr=Label(top1,text=str2,font=16)
    labelr.pack()
    top1.mainloop()
ok=0
def move(event):
    global k
    global ok
    if event.y!=615:
        k=(520-615)/(event.y-615)*(event.x-245)+245
    can.coords(a,245,615,k,520)
    
p=None
op=0
auf=0
t=1
def create(event):
    global p
    global k
    global op
    global auf
    global shots
    global ok
    global sum1
    global t
    if t==1:
        ok=k
        auf=k
        sum1=0
    if event.y!=615 and t==1:
        k1=(525-615)/(event.y-615)*(event.x-245)+245
    if event.y>50 and t==1:
        p=can.create_line(k1,525,k,520,width=5,fill="yellow")
        t=0
        shots+=1
        lab201["text"]=str(shots)+"/7"
        move1()
sum1=0
score=0
top=None
def move1():
    global p
    global k
    global sum1
    global auf
    global op
    global auf
    global score
    global lab101
    global shots
    global top
    global ok
    global t
    sum1+=1
    k2=((520-sum1)-615)*(ok-245)/(520-615)+245
    can.move(p,k2-auf,-1)
    auf=k2
    if (can.coords(rec)[2]>can.coords(p)[0] and can.coords(rec)[0]<can.coords(p)[0]) and can.coords(p)[1]==125:
        score+=1
        can.delete(p)
        t=1
        lab101["text"]=str(score)+"/5"
        if score==5:
            img100=ImageTk.PhotoImage(Image.open("win.png"))
            img101=ImageTk.PhotoImage(Image.open("lose.png"))
            top=Toplevel()
            top.resizable(False, False)
            top.geometry("+{}+{}".format(326, 312))
            top.title("Result of game")
            if shots<=7:
                label2=Label(top,image=img100)
            else:
                label2=Label(top,image=img101)
            label2.pack()
            top.mainloop()
    elif can.coords(p)[1]>0 and can.coords(p)[1]<700 and can.coords(p)[0]>0 and can.coords(p)[0]<500:
        can.update()
        root.after(5,move1)
    else:
        can.delete(p)
        t=1
def moveRec():
    can.move(rec,1,0)
    if can.coords(rec)[2]==500:
        root.after(10,moveRec2)
    else:
       root.after(10,moveRec)
def moveRec2():
    can.move(rec,-1,0)
    if can.coords(rec)[0]==0:
        root.after(10,moveRec)
    else:
       root.after(10,moveRec2)
root=Tk()
root.title("StrikeBullet2021")
root.geometry("500x700")
root.geometry("+{}+{}".format(340, 60))
root.resizable(False, False)
menu=Menu(root,tearoff=0)
root.config(menu=menu)
menu1=Menu(menu,tearoff=0)
menu1.add_command(label="Новая игра",command=def1)
menu1.add_command(label="Оставить отзыв",command=def2)
menu.add_cascade(label="Меню",menu=menu1)
f=Frame(root)
img2=ImageTk.PhotoImage(Image.open("img.png"))
img3=ImageTk.PhotoImage(Image.open("tank2.jpg"))
img4=ImageTk.PhotoImage(Image.open("timer.jpg"))
img100=ImageTk.PhotoImage(Image.open("rato.png"))
can=Canvas(f,width=500,height=700)
can.create_image(0,0,image=img2)
can.create_image(400,34,image=img4)
b=can.create_image(290,34,image=img100)
can.create_image(246,650,image=img3)
a=can.create_line(260,615,260,530,fill="red",arrow=LAST)
can.create_line(276,34,234,34,fill="yellow",arrow=LAST)
rec=can.create_rectangle(215,115,310,125,fill="red")
moveRec()
lab1=Label(text="00",font='Times 20',width=2,height=1)
lab2=Label(text="00",font='Times 20',width=2,height=1)
lab3=Label(text=str(text),font='Times 20',width=2,height=1)
lab100=Label(text="Score",font=28,width=6,height=1).place(x=10,y=10)
lab101=Label(text="0/5",font=28,width=6,height=1,bg="lawn green")
lab200=Label(text="Shots",font=28,width=6,height=1).place(x=85,y=10)
lab201=Label(text="0/7",font=28,width=6,height=1,bg="lawn green")
lab101.place(x=10,y=34)
lab201.place(x=85,y=34)
buttonRes=Button(text="Правила",font=29,width=7,height=2)
buttonRes.bind("<Button-1>",function)
buttonRes.place(x=160,y=10)
lab1.place(x=881,y=24)
lab2.place(x=930,y=24)
lab3.place(x=978,y=24)
root.bind("<Motion>",move)
root.bind("<Button-1>",create)
f.pack()
can.pack(side=LEFT)
startofgame()
root.mainloop()
