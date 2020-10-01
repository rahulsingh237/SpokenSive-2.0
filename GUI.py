from tkinter import *
from speak import *
from app import *
from txttohand import *

root = Tk()

# Icon
root.wm_iconbitmap('notepad.ico')

# Width  x  Height
root.geometry("644x800")

# Fix window size
root.minsize(479,150)
root.maxsize(479,150)

# Title
root.title("SpokenSive - your cursive support")

# Display 
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20") 
screen.pack(fill=X)

# Function
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "C":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"   

        scvalue.set(value)
        print(type(text))
        screen.update()    
   
    elif text == "Reset": #scvalue=text
         try:
            #fullstring = scvalue.get()
            newstring=''
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            
            scvalue.set(newstring)
            os.remove("file\\black.txt")
            os.remove("file\\0outt.png")
            # print(newstring)
            screen.update()
         except Exception as e:
            print(e)
             
    elif text == "voice":
        speech()
        pass
    elif text == "output":
        typing(scvalue.get())
        pass
    elif text == "All Clear":
        scvalue.set("")
        screen.update()
    elif text == "OFF":
        sys.exit()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

# Frame
mFrame = Frame(root)
mFrame.pack(side=TOP, fill=X)


vframe=Frame(mFrame,relief=GROOVE)
vframe.pack(side=TOP)
b=Button(vframe,text="voice",width=20,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)
b=Button(vframe,text="All Clear",width=20,height=3)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)
b=Button(vframe,text="OFF",width=20,height=3)
b.grid(row=0,column=2,padx=15)
b.bind("<Button-1>",click)

topFrame = Frame(root)
topFrame.pack(side=TOP, fill=X)
cframe=Frame(topFrame,relief=GROOVE)
cframe.pack(side=LEFT,padx=80)
b=Button(cframe,text="output",width=20,height=3)
b.pack()
b.bind("<Button-1>",click)

opframe=Frame(topFrame,relief=GROOVE)
opframe.pack(side=TOP,fill=X,padx=10)
b=Button(opframe,text="DEL",width=19,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)

root.mainloop()