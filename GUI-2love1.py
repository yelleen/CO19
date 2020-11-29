from FileIO import *
from Graph import *
from Filtering import *
from tkinter import *

window = Tk()
window.title("CO19")
window.geometry("1280x720")

number = StringVar()
numberChosen = Combobox(window, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)     # 设置下拉列表的值
numberChosen.grid(column=1, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0) 


window.mainloop()