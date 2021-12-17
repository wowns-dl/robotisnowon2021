import tkinter
window=tkinter.Tk()
window.title("계산기")
window.geometry("400x600")
window.resizable(True,True)

now=0
before=0
answer=0
symbol='num'

def save():
    global now
    global before
    before=now
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
    
def clear():
    global now
    now=0
    label.config(text=str(now))
    
def Add():
    global symbol
    save()
    symbol='add'
    label.config(text=str(now))
    
def Sub():
    global symbol
    save()
    symbol='sub'
    label.config(text=str(now))
    
def Mul():
    global symbol
    save()
    symbol='mul'
    label.config(text=str(now))
    
def Div():
    global symbol
    save()
    symbol='div'
    label.config(text=str(now))
    
def Equal():
    global now
    global symbol
    global before
    if symbol=='add':
        now+=before
    elif symbol=='sub':
        now=before-now
    elif symbol=='mul':
        now*=before
    elif symbol=='div':
        if now==0:
            pass
        else:
            now=before/now
    symbol='num'
    label.config(text=str(now))
    
def Period():
    pass
    
label = tkinter.Label(window, text="0",width=30,height=5)
label.place(x=100,y=0)

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
buttonC = tkinter.Button(window,text='C', overrelief="solid", width=11,height=5, command=clear, repeatdelay=1000, repeatinterval=100)
buttonAdd = tkinter.Button(window,text='+', overrelief="solid", width=11,height=5, command=Add, repeatdelay=1000, repeatinterval=100)
buttonSub = tkinter.Button(window,text='-', overrelief="solid", width=11,height=5, command=Sub, repeatdelay=1000, repeatinterval=100)
buttonMul = tkinter.Button(window,text='X', overrelief="solid", width=11,height=5, command=Mul, repeatdelay=1000, repeatinterval=100)
buttonDiv = tkinter.Button(window,text='/', overrelief="solid", width=11,height=5, command=Div, repeatdelay=1000, repeatinterval=100)
buttonEqual = tkinter.Button(window,text='=', overrelief="solid", width=11,height=5, command=Equal, repeatdelay=1000, repeatinterval=100)
buttonPeriod = tkinter.Button(window,text='.', overrelief="solid", width=11,height=5, command=Period, repeatdelay=1000, repeatinterval=100)

button1.place(x=0,y=200)
button2.place(x=100,y=200)
button3.place(x=200,y=200)
button4.place(x=0,y=300)
button5.place(x=100,y=300)
button6.place(x=200,y=300)
button7.place(x=0,y=400)
button8.place(x=100,y=400)
button9.place(x=200,y=400)
button0.place(x=100,y=500)
buttonC.place(x=0,y=500)
buttonAdd.place(x=300,y=300)
buttonSub.place(x=300,y=400)
buttonMul.place(x=300,y=200)
buttonDiv.place(x=300,y=100)
buttonEqual.place(x=300,y=500)
buttonPeriod.place(x=200,y=500)

window.mainloop()
