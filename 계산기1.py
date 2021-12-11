from tkinter import*

window=tkinter.Tk()
window.title("계산기")
window.geometry("400x600")
window.resizable(False, False)

count=0

def one():
    global count
    count +=1
    label.config(text=str(count))

label = tkinter.Label(window, text="0")
label.place(x=200,y=0)

button1 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button2 = tkinter.Button(window, overrelief="solid", width=11,height=5, command=one, repeatdelay=1000, repeatinterval=100)
button1.place(x=0,y=100)
button2.place(x=100,y=100)

window.mainloop()
