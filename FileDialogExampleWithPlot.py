__author__ = 'Griff'

#This is the answer to Assignment 2_2 including the matplotlib plot
#It demonstrates how to use the tkinter file dialog to open a file
#and how to generate a scatter plot in matplotlib

from tkinter import *
from tkinter import filedialog as FD #file dialog to help find data files
import matplotlib #matplotlib imports must be done in this order
matplotlib.use('TkAgg')#this is the preferred tkinter backend, program crashes without
matplotlib.interactive(True)
import matplotlib.pyplot as plt

window=Tk()#explicitely create tkinter window
Tk.withdraw(window)#make it disappear
#Define variables to hold data
DataFile = []#Used for resaving the data
Xval = []#Used for plotting
Yval = []#Used for plotting
#Function to read data from file
def loadData():
    window.update()
    NFile = FD.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    window.update()
    with open(NFile) as f:
        for line in f:
            data = line.split(",")
            DataFile.extend([int(data[0]),int(data[1])])
            Xval.append(int(data[0]))
            Yval.append(int(data[1]))
            print(data)
    f.closed
    print(DataFile) #Test that data is OK
    print(Xval, Yval)#Test that correct values are in X and Y
#Function to save the changed data to file
def saveXYData(XYData):
    NFile = FD.asksaveasfilename(defaultextension='.txt',filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    with open(NFile,"w+") as f:
        for i in range(0,int(len(DataFile)/2)):
            f.write(str(DataFile[2*i]) +" \t" + str(DataFile[(2*i)+1]) + "\n")
    f.close()

#function to get user to input additional data
def addDataToFile():
    NewX = int(input("What is your new X value "))#prompt for new X value
    Xval.append(NewX)#add to Xval
    NewY = int(input("What is your new Y value "))#prompt for new Y value
    Yval.append(NewY)#add to Yval
    DataFile.extend([NewX,NewY])#add both X and Y to DataFile
    print(DataFile)#check DataFile

loadData()#call function to read data in
fig, (ax1,ax2) = plt.subplots(1,2)#set up matplotlib figure with two plots
ax1.set_ylabel("income (millions)")
ax1.tick_params(axis="both",direction = "in")#for fun put tick marks on inside
ax1.set_title("Income Projection")
ax1.set_xlabel("years")
ax1.set_xlim(0,8)#define x and y limits so both plots have same size
ax1.set_ylim(0,14)#define x and y limits so both plots have same size
ax1.scatter(Xval, Yval)#create scatter plot on first plot
#ax2.scatter([0,0],[0,0])
#plt.ion()
plt.show()#This isn't working for a reason that I don't understand
addDataToFile()#call to add more data
ax2.scatter(Xval, Yval)#make scatter plot on second set of axes
ax2.set_xlabel("years")
ax2.set_ylabel("amount of stress (%gray hairs)")
ax2.set_title("Stress Expectation")
ax2.set_xlim(0,8)#define x and y limits so both plots have same size
ax2.set_ylim(0,14)#define x and y limits so both plots have same size
fig.tight_layout()#this is needed so that the y label on the 2nd plot has space
plt.show()#plot appears
plt.savefig("Assignment2_2Figure.png")
saveXYData(DataFile)

#the following issues I haven't been able to fix:
#  1.  I can't get the first plot to appear without the second
#
