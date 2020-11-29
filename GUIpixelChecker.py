from FileIO import *
from Graph import *
from Filtering import *
from tkinter import *

window = Tk()
window.title("CO19")
window.geometry("1280x720")

pix = PhotoImage(file ="G:\\daein\\CO19\\1180700.png")

label1 = Label(window, image= pix )

label1.pack()

window.mainloop()