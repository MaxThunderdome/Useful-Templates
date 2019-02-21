from tkinter import *
master = Tk()
width = 800
height = 800
xborder=50
yborder = 25
w = Canvas(master, width=width, height=height)
w.pack()
colors = ["blue","red","green","yellow"]
"""
w.create_line(0, 0, width, height) 
w.create_line(0, height, width, 0, fill="red", dash=(4, 4)) """
for i in range(0,10):
    for j in range(0,10):
        w.create_rectangle(i*50,j*50, (i*50)+50 , (j*50)+50,fill=colors[(i+j)%4])

mainloop()