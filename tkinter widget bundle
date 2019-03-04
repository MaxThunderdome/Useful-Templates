from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plot
#the following line is needed in order to place a matplotlib plot inside the tkinter window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

TopLevel = Tk()
TopLevel.title("Chem270_Widgets")
TopLevel.minsize = "1000 x 1000"


#dummy functions to handle menu selection

def New_clicked():
    print("New clicked")

def Open_clicked():
    print("Open clicked")

def Save_clicked():
    print("Save clicked")

def SaveAs_clicked():
    print("Save As clicked")

def Cut_clicked():
    print("Cut clicked")

def Copy_clicked():
    print("Copy clicked")

def Paste_clicked():
    print("Paste clicked")

def Delete_clicked():
    print("Delete clicked")

def Quit_clicked():
    raise SystemExit


#Create Menu Bar
main_menu = Menu(TopLevel)

FileMenu = Menu(main_menu)
FileMenu.add_command(label="New",command = New_clicked)
FileMenu.add_separator()
FileMenu.add_command(label="Open",command = Open_clicked)
FileMenu.add_command(label="Save",command = Save_clicked)
FileMenu.add_command(label="Save As",command = SaveAs_clicked)
FileMenu.add_separator()
FileMenu.add_command(label="Quit Demo",command = Quit_clicked)

EditMenu = Menu(main_menu)
EditMenu.add_command(label="Cut",command = Cut_clicked)
EditMenu.add_command(label="Copy",command = Copy_clicked)
EditMenu.add_command(label="Paste",command = Paste_clicked)
EditMenu.add_command(label="Delete",command = Delete_clicked)


main_menu.add_cascade(label = "File", menu = FileMenu)
main_menu.add_cascade(label = "Edit", menu = EditMenu)

#Create Tabs

style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [50, 20] },}})

style.theme_use("MyStyle")

tab_control = ttk.Notebook(TopLevel)
buttonTab = ttk.Frame(TopLevel)
otherWidgetsTab = ttk.Frame(TopLevel)
pictureTab = ttk.Frame(TopLevel)
plotTab = ttk.Frame(TopLevel)
tab_control.add(buttonTab,text = "Buttons")
tab_control.add(otherWidgetsTab,text = "Other Widgets")
tab_control.add(pictureTab,text = "Picture")
tab_control.add(plotTab,text = "Plot")
tab_control.grid(column = 0, row = 0,sticky = NSEW)


#functions for First Tab
def bclicked():
    print("button was clicked")
    button1.config(text ="You clicked me")

buttonTab.columnconfigure(0,weight = 1)
buttonTab.columnconfigure(1,weight = 1)
#Create Content for First Tab
buttonheight = 2
buttonwidth = 5
Label1 = Label(buttonTab,text = "You are viewing the button tab",wraplength = 120, justify = LEFT)
Label1.grid(column = 0, row = 1)
button1 = Button(buttonTab,text = "button1",bg = "blue",fg = "red", command = bclicked)
button2 = Button(buttonTab,text = "button2",height = buttonheight, width = buttonwidth)
button3 = Button(buttonTab,text = "button3",height = buttonheight, width = buttonwidth)
button4 = Button(buttonTab,text = "button4",height = buttonheight, width = buttonwidth)
button1.grid(column = 0,row = 2,sticky = NSEW)
button2.grid(column = 1,row = 2,sticky = NSEW)
button3.grid(column = 0,row = 3,sticky = NSEW)
button4.grid(column = 1,row = 3,sticky = NSEW)

def button5clicked():
    str1 = "You entered " + textIn.get()
    Label2.config(text = str1)

#Create Content for Second Tab
Label2 = Label(otherWidgetsTab,text = "You are viewing the second tab")
Label2.grid(column = 0, row = 1)
textIn = Entry(otherWidgetsTab, width = 20)
textIn.grid(column = 1, row = 1)
button5 = Button(otherWidgetsTab, text = "click after entering text", command = button5clicked)
button5.grid(column = 0, row = 2)
#add a combobox
combo1 = ttk.Combobox(otherWidgetsTab)
combo1['values'] = (2,4,6,8,10,"Text")
combo1.current(1)
combo1.grid(column = 0, row = 3)
#add scrolled text
# sText = scrolledtext.ScrolledText(otherWidgetsTab,width = 20,height = 10)
# sText.insert(INSERT,"I can pretty much go on writing forever.  This will scroll, so I can just keep writing and writing and eventually it will scroll")
# sText.grid(column = 1, row = 3)

#Create Content for Third Tab
Label3 = Label(pictureTab,text = "You are viewing the third tab",font = ("Arial Bold",25))
Label3.grid(column = 2, row = 0)
#Create a picture
Tab3Canvas = Canvas(pictureTab, width = 400,height = 400)
Tab3Canvas.grid(column = 2, row = 1)
Tab3Canvas.create_line(0,0,400,400,fill = "black")
colorarray = ['red','blue','yellow']
for i in range(0,10):
    for j in range(0,10):
        Tab3Canvas.create_rectangle(100+(20*i),100+(20*j),(20*i)+120,(20*j)+120,fill=colorarray[(i+j)%3])


#Create Content for Plot tab
x_values = [0,1,2,3,4,5]
y_values = [2,4,6,8,10,12]

fig, ax  = plot.subplots(figsize=(4,5))

ax.scatter(x_values,y_values)
ttk.Label(plotTab,text = "test plot").grid(column = 0,row = 0)
fig.suptitle("test plot")
ax.set_xlabel("some x values", fontsize = 12)
ax.set_ylabel("some y values", fontsize = 16)
canvas = FigureCanvasTkAgg(fig, master = plotTab)
canvas.get_tk_widget().grid(column = 0, row = 0)


#TopLevel.grid_propagate(0)
TopLevel.config(menu=main_menu)
TopLevel.mainloop()
