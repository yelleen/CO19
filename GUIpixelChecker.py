'''
from FileIO import *
from Graph import *
from Filtering import *
'''
from tkinter import *

window = Tk()
window.title("CO19")
window.geometry("1280x720")

datapath = "1180700.png"

pix = PhotoImage(file = datapath)

label1 = Label(window, image= pix )

label1.pack()

window.mainloop()