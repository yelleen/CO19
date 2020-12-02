from GUI_Info import *
from FileIO import *
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog

window = Tk()
window.title("CO19")
window.geometry("1280x720")
window.resizable(False, False)

#fileName = "" 나중에 없애기 -> 리팩토링: Get(), Set()
People = []
pe = []
phoneCorrect = True
#Region Registering
def isCorrectPhoneNumber():
    global phoneCorrect
    phoneStr = str(entryPhoneNumber.get())
    if len(phoneStr) != 13:
        phoneCorrect = False
    else:
        for i in range(13):  
            if phoneStr[i] == '-' and (i == 3 or i == 8):
                phoneCorrect = False
            elif phoneStr[i].isdigit():
                phoneCorrect = False
    WarningPhone()
def WarningPhone():
    global phoneCorrect
    if phoneCorrect == False:
        result = messagebox.showinfo(title = "경고", message = "전화번호가 잘못 입력되었습니다.\n다시 입력해주세요.\n'010-####-####'")
    else:
        Register()

def entryToList():
    global pe
    pe.append(str(entryName.get()))
    pe.append(str(entryAge.get()))
    pe.append(str(comboboxGender.get()))
    pe.append(str(entryPhoneNumber.get()))
    pe.append(str(comboboxAdr1.get()))
    pe.append(str(comboboxAdr2.get()))

def Register():
    global People, pe
    p = Person(pe[0], pe[1], pe[2], pe[3], pe[4], pe[5], pe[6], pe[7], pe[8])
    People.append(p)
#EndRegion
#Region Finding
def Find(pe):
    global People
#EndRegion
#Region Save
def Save():
    global People, fileName
    fileName = filedialog.askopenfilename(initaldir = '/', title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    AddPersonToFile(fileName, People)
#EndRegion
#Region Load
def Load(pe):
    global People
    fileName = filedialog.askopenfilename(initaldir = '/', title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    pStrList = ReadText(fileName)
    for pStr in pStrList:
        StringToPerson(pStr, People)
#EndRegion

'''
=====================================================================================
'''

btn_register = Button(window, text = "등록하기", command = Register)
btn_finding = Button(window, text = "찾기", command = Find)

labelName = Label(window, text = "이름", width = 4, height = 1, font = "나눔바른고딕 -28", anchor="nw")
entryName = Entry(window, width = 15, font = "나눔바른고딕 -28")

labelAge = Label(window, text = "나이", width = 4, height = 1, font = "나눔바른고딕 -28", anchor="nw")
entryAge = Entry(window, width = 15, font = "나눔바른고딕 -28")

genderValue = gender
labelGender = Label(window, text = "성별", width = 4, height = 1, font = "나눔바른고딕 -28", anchor="nw")
comboboxGender = ttk.Combobox()

labelPhoneNumber = Label(window, text = "전화번호", width = 8, height = 1, font = "나눔바른고딕 -28", anchor="nw")
entryPhoneNumber = Entry(window, width = 15, font = "나눔바른고딕 -28")

adr1Value = adr1
labelAddress1 = Label(window, text = "주소", width = 4, height = 1, font = "나눔바른고딕 -28", anchor="nw")
comboboxAdr1 = ttk.Combobox(window, height = 15, values = adr1Value, font = "나눔바른고딕 -26")

adr2Value = ()
if str(comboboxAdr1.get()) == adr1[0]:
    adr2Value = adrA
elif str(comboboxAdr1.get()) == adr1[1]:
    adr2Value = adrB
else:
    adr2Value = adrC

labelAddress2 = Label(window, text = " ", width = 1, height = 1, font = "나눔바른고딕 -28")
comboboxAdr2 = ttk.Combobox(window, height = 15, values = adr2Value, font = "나눔바른고딕 -26")

labelTimeIn = Label(window, text = "들어온 시간", width = 8, height = 1, font = "나눔바른고딕 -28")
entryTimeIn = Entry(window, width = 8, font = "나눔바른고딕 -28")

labelTimeOut = Label(window, text = "나간 시간", width = 8, height = 1, font = "나눔바른고딕 -28")
entryTimeOut = Entry(window, width = 8, font = "나눔바른고딕 -28")

'''
========================================================================
'''
labelName.place(x = 100, y = 100, width=100, height=30)# 명칭 표시
entryName.place(x = 100, y = 150, width=200, height=50)# 입력란 표시
labelAge.place(x = 400, y = 100, width=100, height=30)
entryAge.place(x = 400, y = 150, width=100, height=50)
labelGender.place(x = 600, y = 100, width=100, height=30)
comboboxGender.place(x = 600, y = 150, width=100, height=50)
labelAddress1.place(x = 800, y = 100, width=100, height=30)
comboboxAdr1.place(x = 800, y = 150, width=150, height=50)
comboboxAdr2.place(x = 960, y = 150, width=150, height=50)

#두번쨰 줄 표시할 것들 
labelPhoneNumber.place(x = 100, y = 250, width=120, height=50)
entryPhoneNumber.place(x = 100, y = 300, width=250, height=50)

btn = Button(window, width = 20, command = isCorrectPhoneNumber)
btn.place(x = 400, y = 250, width=150, height=50)


window.mainloop()
