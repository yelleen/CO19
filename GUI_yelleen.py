#from FileIO import *
#from Graph import *
#from Filtering import *
from GUI_Info import *
from tkinter import Tk, Label, Button, Entry, ttk

def entryToString():
    s = str(entryName.get()) + ' ' + str(entryAge.get()) + ' ' + str(comboboxGender.get()) + ' ' + str(entryPhoneNumber.get()) + ' ' + str(comboboxAdr1.get()) + ' ' + str(comboboxAdr2.get())
    return s

window = Tk()
window.title("CO19")
window.geometry("1280x720")
window.resizable(False, False)

labelName = Label(window, text = "이름", width = 4, height = 1, font = "나눔바른고딕 -28")
entryName = Entry(window, width = 15, font = "나눔바른고딕 -28")

labelAge = Label(window, text = "나이", width = 4, height = 1, font = "나눔바른고딕 -28")
entryAge = Entry(window, width = 15, font = "나눔바른고딕 -28")

genderValue = gender
labelGender = Label(window, text = "성별", width = 4, height = 1, font = "나눔바른고딕 -28")
comboboxGender = ttk.Combobox(window, height = 15, values = genderValue)

labelPhoneNumber = Label(window, text = "전화번호", width = 8, height = 1, font = "나눔바른고딕 -28")
entryPhoneNumber = Entry(window, width = 15, font = "나눔바른고딕 -28")

adr1Value = adr1
labelAddress1 = Label(window, text = "주소", width = 4, height = 1, font = "나눔바른고딕 -28")
comboboxAdr1 = ttk.Combobox(window, height = 15, values = adr1Value)

adr2Value = ()
if str(comboboxAdr1.get()) == adr1[0]:
    adr2Value = adrA
elif str(comboboxAdr1.get()) == adr1[1]:
    adr2Value = adrB
else:
    adr2Value = adrC
labelAddress2 = Label(window, text = " ", width = 1, height = 1, font = "나눔바른고딕 -28")
comboboxAdr2 = ttk.Combobox(window, height = 15, values = adr2Value)

labelTimeIn = Label(window, text = "들어온 시간", width = 8, height = 1, font = "나눔바른고딕 -28")
entryTimeIn = Entry(window, width = 8, font = "나눔바른고딕 -28")

labelTimeOut = Label(window, text = "나간 시간", width = 8, height = 1, font = "나눔바른고딕 -28")
entryTimeOut = Entry(window, width = 8, font = "나눔바른고딕 -28")

def test():
    print(str(comboboxGender.get()))

btn = Button(window, width = 20, command = test)

btn.pack()
labelName.pack()
entryName.pack()
labelAge.pack()
entryAge.pack()
labelGender.pack()
comboboxGender.pack()
labelPhoneNumber.pack()
entryPhoneNumber.pack()
labelAddress1.pack()
comboboxAdr1.pack()
labelAddress2.pack()
comboboxAdr2.pack()




'''
labelName.place(x = 20, y = 50)
entryName.place(x = 20, y = 90)
labelPhoneNumber.place(x = 270, y = 50)
entryPhoneNumber.place(x = 270, y = 90)
labelAddress1.place(x = 520, y = 50)
entryAddress1.place(x = 520, y = 90)
labelAddress2.place(x = 658, y = 50)
entryAddress2.place(x = 658, y = 90)
'''

window.mainloop()
