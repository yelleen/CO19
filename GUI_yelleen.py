from FileIO import *
#from Graph import *
#from Filtering import *
from GUI_Info import *
from tkinter import Tk, Label, Button, Entry, ttk

People = []

def ReadTextToPeople():
    global People
    People = ReadText("2020_11_1")

def entryToString():
    s = str(entryName.get()) + ' ' + str(entryAge.get()) + ' ' + str(comboboxGender.get()) + ' ' + str(entryPhoneNumber.get()) + ' ' + str(comboboxAdr1.get()) + ' ' + str(comboboxAdr2.get())
    return s

window = Tk()
window.title("CO19")
window.geometry("1280x720")
window.resizable(False, False)

labelName = Label(window, text = "이름", width = 4, height = 1, font = "나눔바른고딕 -28")
entryName = Entry(window, width = 15)

labelAge = Label(window, text = "나이", width = 4, height = 1, font = "나눔바른고딕 -28")
entryAge = Entry(window, width = 15)

genderValue = gender
labelGender = Label(window, text = "성별", width = 4, height = 1, font = "나눔바른고딕 -28")
comboboxGender = ttk.Combobox(window, height = 15, values = genderValue)

labelPhoneNumber = Label(window, text = "전화번호", width = 8, height = 1, font = "나눔바른고딕 -28")
entryPhoneNumber = Entry(window)

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
entryTimeIn = Entry(window, width = 8)

labelTimeOut = Label(window, text = "나간 시간", width = 8, height = 1, font = "나눔바른고딕 -28")
entryTimeOut = Entry(window, width = 8)

def test():
    print(str(comboboxGender.get()))

btnA = Button(window, text = "A", width = 20, command = ReadTextToPeople)
btnB = Button(window, text = "B", width = 20, command = test)
btnC = Button(window, text = "C", width = 20, command = test)
btnD = Button(window, text = "D", width = 20, command = test)

btnA.grid(row = 0, column = 0)
btnB.grid(row = 0, column = 1)
btnC.grid(row = 0, column = 2)
btnD.grid(row = 0, column = 3)

labelName.grid(row = 1, column = 0)
entryName.grid(row = 1, column = 1)
labelAge.grid(row = 2, column = 0)
entryAge.grid(row = 2, column = 1)
labelGender.grid(row = 3, column = 0)
comboboxGender.grid(row = 3, column = 1)
labelPhoneNumber.grid(row = 4, column = 0)
entryPhoneNumber.grid(row = 4, column = 1)
labelAddress1.grid(row = 5, column = 0)
comboboxAdr1.grid(row = 5, column = 1)
labelAddress2.grid(row = 6, column = 0)
comboboxAdr2.grid(row = 6, column = 1)

window.mainloop()
