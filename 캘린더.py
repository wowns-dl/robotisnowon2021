import tkinter

 = (January,February,March,April,May,June,July,August,September,October,November,December)

window = tkinter.Tk()

window.title("Calendar")
window.geometry("640x400")
window.resizable(True, True)

def test():
    pass


#config

Month = tkinter.Label(window, text = Month[], width = 10, height = 5, fg = "red", relief = "solid")

Left_Button = tkinter.Button(window, text = '<', overrelief = "solid", command = , repeatdelay=1000, repeatinterval=100)
Right_Button = tkinter.Button(window, text = '>', overrelief = "solid", command = test, repeatdelay=1000, repeatinterval=100)


Left_Button.place(width = 50, height = 50, x = 0, y = 0)
Right_Button.place(width = 50, height = 50, x = 590, y = 0)







window.mainloop()
