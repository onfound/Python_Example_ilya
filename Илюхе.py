import random
from random import random
from tkinter import *
import tkinter
root=Tk()
root.title('Random Example')
root.geometry('300x250')
c=Canvas(root,width=300,height=250,bg='lightblue')
tex=Text(c,width=30,height=3,bd=2,font="Arial 12",wrap=WORD,bg="gainsboro")
ent=Entry(c,width=20,font="Arial 14",bd=3,bg="gainsboro")
but=Button(c,width=25,height=1,font='Arial 12', bg='gold',
           fg='black',text='Генерировать пример')
c.create_text(200,240, text="by ilya_dolgushev",
                          font="arial 8",fill="black",anchor="w")

def otvet (event):
    tex.delete(1.0,END)
    v=ent.get()
    if v=='':
        result='Введи число xD'
    else:
        n1=int(v)
        randomNumber1=int(random()*200)
        randomNumber2=int(random()*200)
        randomNumber3=randomNumber1+randomNumber2-n1
        result=randomNumber1,'+',randomNumber2,'-',randomNumber3
    tex.insert(END,result)
    
but.bind('<Button-1>',otvet)
root.bind('<Return>',otvet)

tex.grid(row=1,column=0,padx=12,pady=20)
ent.grid(row=2,column=0,padx=12)
but.grid(row=3,column=0,pady=10)
c.pack(side=LEFT,fill=BOTH,expand=2)
mainloop()

