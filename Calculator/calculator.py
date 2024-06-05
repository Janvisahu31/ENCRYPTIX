from tkinter import *


def click(event):
    global strval
    text=event.widget.cget("text")
    
    if text=="=":
        if strval.get().isdigit():
            value=int(strval.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        strval.set(value)
        screen.update()
    elif text=="C":
        strval.set("")
    else:
        strval.set(strval.get()+ text)
        screen.update()
    
        

    
root=Tk()
root.geometry("550x700")
root.minsize(550,700)
root.maxsize(550,700)
root.title("Calculator")


strval=StringVar()
strval.set("")
screen=Entry( root,textvar=strval,font="sans 50 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text="C",font="sans 30 bold",padx=100,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="%",font="sans 30 bold",padx=35,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="/",font="sans 30 bold",padx=42,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f1.pack(fill=X,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text="9",font="sans 33 bold",padx=35,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="8",font="sans 30 bold",padx=39,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="7",font="sans 30 bold",padx=41,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="*",font="sans 30 bold",padx=37,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f1.pack(fill=X,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text="6",font="sans 33 bold",padx=35,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="5",font="sans 30 bold",padx=39,pady=25)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="4",font="sans 30 bold",padx=41,pady=25)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="-",font="sans 30 bold",padx=39,pady=25)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f1.pack(fill=X,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text="3",font="sans 33 bold",padx=35,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="2",font="sans 30 bold",padx=39,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="1",font="sans 30 bold",padx=41,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="+",font="sans 30 bold",padx=35,pady=23)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f1.pack(fill=X,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text=".",font="sans 41 bold",padx=35,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="0",font="sans 30 bold",padx=38,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f1,text="=",font="sans 30 bold",padx=600,pady=20)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f1.pack(fill=X,padx=10)


root.mainloop()
