import tkinter
window=tkinter.Tk()
window.title("계산기")
window.geometry("300x500")
window.resizable(True,True)

now=0

def one():
    global now
    now +=1
    label.config(text=str(now))

label = tkinter.Label(window, text="0",width=5,height=5)
label.place(x=128,y=0)

button1 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button2 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button3 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button4 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button5 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button6 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button7 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button8 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button9 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button0 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
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
