import tkinter
window=tkinter.Tk()
window.title("계산기")
window.geometry("300x500")
window.resizable(True,True)

now=0

def rnlcksg():
    global now
    now=now*10

def one():
    global now
    rnlcksg()
    now+=1
    label.config(text=str(now))
    
def two():
    global now
    rnlcksg()
    now+=2
    label.config(text=str(now))
    
def three():
    global now
    rnlcksg()
    now+=3
    label.config(text=str(now))
    
def four():
    global now
    rnlcksg()
    now+=4
    label.config(text=str(now))
    
def five():
    global now
    rnlcksg()
    now+=5
    label.config(text=str(now))
    
def six():
    global now
    rnlcksg()
    now+=6
    label.config(text=str(now))
    
def seven():
    global now
    rnlcksg()
    now+=7
    label.config(text=str(now))
    
def eight():
    global now
    rnlcksg()
    now+=8
    label.config(text=str(now))
    
def nine():
    global now
    rnlcksg()
    now+=9
    label.config(text=str(now))
    
def zero():
    global now
    rnlcksg()
    now+=0
    label.config(text=str(now))
    
    

label = tkinter.Label(window, text="0",width=30,height=5)
label.place(x=50,y=0)

button1 = tkinter.Button(window,text='1', overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button2 = tkinter.Button(window,text='2', overrelief="solid", width=11,height=5, command=two, repeatdelay=1000, repeatinterval=100)
button3 = tkinter.Button(window,text='3', overrelief="solid", width=11,height=5, command=three, repeatdelay=1000, repeatinterval=100)
button4 = tkinter.Button(window,text='4', overrelief="solid", width=11,height=5, command=four, repeatdelay=1000, repeatinterval=100)
button5 = tkinter.Button(window,text='5', overrelief="solid", width=11,height=5, command=five, repeatdelay=1000, repeatinterval=100)
button6 = tkinter.Button(window,text='6', overrelief="solid", width=11,height=5, command=six, repeatdelay=1000, repeatinterval=100)
button7 = tkinter.Button(window,text='7', overrelief="solid", width=11,height=5, command=seven, repeatdelay=1000, repeatinterval=100)
button8 = tkinter.Button(window,text='8', overrelief="solid", width=11,height=5, command=eight, repeatdelay=1000, repeatinterval=100)
button9 = tkinter.Button(window,text='9', overrelief="solid", width=11,height=5, command=nine, repeatdelay=1000, repeatinterval=100)
button0 = tkinter.Button(window,text='0', overrelief="solid", width=11,height=5, command=zero, repeatdelay=1000, repeatinterval=100)
button1.place(x=0,y=100)
button2.place(x=100,y=100)
button3.place(x=200,y=100)
button4.place(x=0,y=200)
button5.place(x=100,y=200)
button6.place(x=200,y=200)
button7.place(x=0,y=300)
button8.place(x=100,y=300)
button9.place(x=200,y=300)
button0.place(x=100,y=400)

window.mainloop()
