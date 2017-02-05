from tkinter import *
from alarmParse import Parser
from tkinter import filedialog
from bs4 import BeautifulSoup
import pandas
from os import path

window=Tk()


filename=""
def open_file():
    filename=filedialog.askopenfilename()
    e1_value.set(filename)
    return filename

def filename():
    filename=e1.get()
    excelName=e2.get()
    parser=Parser(filename)
    alarms=r1_value.get()
    bacnet=r2_value.get()
    histories=r3_value.get()
    parser.reportBuilder(excelName,alarms,histories,bacnet)
    print(alarms,bacnet,histories)
l1=Label(window,text="config.xml file")
l1.grid(row=0,column=0)

command=lambda: button('hey')
b1=Button(window,text="Open",command=lambda: open_file())
b1.grid(row=0,column=2)


#b1=Button(window,text="Convert",command=kg_conversion)
#b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)


#e1_value.set(filename)

l2=Label(window,text="excel file name")
l2.grid(row=2,column=0)


e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=2,column=1)


b2=Button(window,text="Create Excel",command=filename)
b2.grid(row=2,column=2)

r1_value=IntVar()
r1=Radiobutton(window,text="Alarms",variable=r1_value,value=1)
r1.grid(row=1,column=0)
r1.deselect()

r2_value=IntVar()
r2=Radiobutton(window,text="Histories",variable=r2_value,value=2)
r2.grid(row=1,column=1)

r3_value=IntVar()
r3=Radiobutton(window,text="BACnet",variable=r3_value,value=3)
r3.grid(row=1,column=2)

window.mainloop()
