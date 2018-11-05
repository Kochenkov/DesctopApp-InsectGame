from tkinter import *


c = 200
d = 200
e = 28
f = 28
a = (c-e)/2
b = (d-f)/2

z = 0 # переменная для остановки работы программы при нажатии SMASH

def right_(event) :
    global a,b,c,d,z
    if z==0:
        if a<(c-e):
            a=a+1
            if a%2==0:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=RIGHT1)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
               
               
            else:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=RIGHT2)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
               
              
              
               
    else:
        l = Label(root, image=SMASH)
        l["bg"]="white"
        l.place(x = a, y = b)
       


        
def left_(event) :
    global a,b,c,d,z
    if z==0:
        if a>0:
            a=a-1
            if a%2==0:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=LEFT1)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
            else:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=LEFT2)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
               
    else:
        l = Label(root, image=SMASH)
        l["bg"]="white"
        l.place(x = a, y = b)
        


    
def up_(event) :
    global a,b,c,d,z
    if z==0:
        if b>0:
            b=b-1
            if b%2==0:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=UP1)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
            else:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=UP2)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
               
    else:
        l = Label(root, image=SMASH)
        l["bg"]="white"
        l.place(x = a, y = b)
        



        
def down_(event) :
    global a,b,c,d,z
    if z==0:
        if b<(d-f):
            b=b+1
            if b%2==0:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=DOWN1)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
            else:
               canv = Canvas(root,width=c,height=d,bg="white")
               canv.place(x = -2, y = -2)
               l=Label(root, image=DOWN2)
               l.place(x = a, y = b)
               l["bg"]="white"
               l.bind('<Button-1>',smash_)
               
    else:
        l = Label(root, image=SMASH)
        l["bg"]="white"
        l.place(x = a, y = b)
    


        

def smash_(event) :
    global z
    z = 1
    l = Label(root, image=SMASH)
    l["bg"]="white"
    l.place(x = a, y = b)

    
def close(event):
    btn.place_forget()
    root.bind('d', right_)
    root.bind('a', left_)
    root.bind('w', up_)
    root.bind('s', down_)
   





    
root=Tk()
root.title('ЖУК')
root["bg"] = "white"
root.minsize(width = c, height = d)
root.maxsize(width = c, height = d)



UP1 = PhotoImage(file='images/UP1.gif')
DOWN1 = PhotoImage(file='images/DOWN1.gif')
LEFT1 = PhotoImage(file='images/LEFT1.gif')
RIGHT1 = PhotoImage(file='images/RIGHT1.gif')

UP2 = PhotoImage(file='images/UP2.gif')
DOWN2 = PhotoImage(file='images/DOWN2.gif')
LEFT2 = PhotoImage(file='images/LEFT2.gif')
RIGHT2 = PhotoImage(file='images/RIGHT2.gif')

SMASH = PhotoImage(file='images/SMASH.gif')

canv = Canvas(root,width=c,height=d,bg="white")
canv.place(x = -2, y = -2)


l = Label(root, image=UP1)
l.bind('<Button-1>',smash_)
l["bg"]="white"
l.place(x = a, y = b)

btn = Button(root, text='''Добро пожаловать
в имитатор управления жуком!
Управление осуществляется
клавишами a s w d
(английская раскладка).
Нажав на жука мышкой,
вы убъёте его.
-------------------------------
Что бы начать игру,
нажмите на эту кнопку.''')

btn.place(x = 10, y = 10)
btn.bind('<Button-1>',close)



root.mainloop()
