from tkinter import *

TopLevel = Tk()
TopLevel.title("Chem270 Button Demo")
TopLevel.minsize = "600 x 600"
bw = 30
bh = 10
#dummy functions to handle button clicks
def button1_clicked():
    print("button 1 clicked")

def button2_clicked():
    print("button 2 clicked")

def button3_clicked():
    print("button 3 clicked")

def button4_clicked():
    print("button 4 clicked")

Label1 = Label(TopLevel,text = "You are viewing the button tab",wraplength = 120, justify = LEFT)
Label1.grid(column = 0, row = 1)
button1 = Button(TopLevel,text = "button1", command = button1_clicked, height = bh, width = bw)
button2 = Button(TopLevel,text = "button2", command = button2_clicked, height = bh, width = bw)
button3 = Button(TopLevel,text = "button3", command = button3_clicked, height = bh, width = bw)
button4 = Button(TopLevel,text = "button4", command = button4_clicked, height = bh, width = bw)
button1.grid(column = 0,row = 2,sticky = N+S+E+W)
button2.grid(column = 1,row = 2,sticky = N+S+E+W)
button3.grid(column = 0,row = 3,sticky = N+S+E+W)
button4.grid(column = 1,row = 3,sticky = N+S+E+W)

TopLevel.mainloop()
