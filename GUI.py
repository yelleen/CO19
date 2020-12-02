from FileIO import Person, LoadFile, SaveFile, toPerson
from GUI_Info import *
from Filtering import FilterByName, FilterByPhoneNumber, FilterByAddress, FilterByStay
from Graph import CreateBarGraph, CreateLineGraph, CreateCircleGraph
from tkinter import Tk, Toplevel, ttk, messagebox, filedialog, Label, Entry, Button, Listbox, Canvas
#Region Field
isCorrect = True # to check phone number format
#EndRegion
#Region WindowCreate
window = Tk()
window.title("CO19SEARCH")
window.geometry("1280x720")
window.resizable(False, False)
#EndRegion
#Region Registering
def CheckPhoneNumber():
    global isCorrect
    phone_string = str(ent_phone_number.get())
    if len(phone_string) != 13:
        phone_string = False
    else:
        for i in range(13):
            if phone_string[i] == '-' and (i == 3 or i == 8):
                isCorrect = False
            elif phone_string[i].isdigit():
                isCorrect = False
    if isCorrect == False:
        messagebox.showinfo(title = "경고", message = "전화번호가 잘못 입력되었습니다.\n다시 입력해주세요.\n'010-####-####'")
    else:
        Registering()
def Registering():
    person_string = ""
    person_string += str(ent_name.get()) + ' '
    person_string += str(cbx_age.get()) + ' '
    person_string += str(cbx_gender.get()) + ' '
    person_string += str(ent_phone_number.get()) + ' '
    person_string += str(cbx_address1.get()) + ' '
    person_string += str(cbx_address2.get()) + ' '
    person_string += str(cbx_time_in_hour.get()) + ':'
    person_string += str(cbx_time_in_min.get()) + ' '
    person_string += str(cbx_time_out_hour.get()) + ':'
    person_string += str(cbx_time_out_min.get()) + ' '
    person_string += str(cbx_room_number.get()) + '\n'
    toPerson(person_string)
#EndRegion
#Region Finding
def Finding():
    newWindow = Toplevel(window)
    newWindow.title("Searching")
    newWindow.geometry("1280x720")
    newWindow.resizable(False, False)
    #Method
    def ShowList(people):
        count = 0
        for person in people:
            lbx_people.insert(count, person.toString())
            count += 1
    def FilteringName():
        searching_by = str(ent_filter_by_name.get())
        searching_people = FilterByName(searching_by)
        ShowList(searching_people)
    def FilteringPhoneNumber():
        searching_by = str(ent_filter_by_phone_number.get())
        searching_people = FilterByPhoneNumber(searching_by)
        ShowList(searching_people)
    def FilteringAddress():
        searching_by_array = []
        searching_by_array.append(str(cbx_filter_by_address1.get()))
        searching_by_array.append(str(cbx_filter_by_address2.get()))
        searching_people = FilterByAddress(searching_by_array)
        ShowList(searching_people)
    def FilteringTime():
        searching_by_array = []
        searching_by_array.append(int(cbx_filter_by_address1.get()))
        searching_by_array.append(int(cbx_filter_by_address2.get()))
        searching_people = FilterByStay(searching_by_array)
        ShowList(searching_people)
    #Widget Create
    #btn: button, ent: entry, cbx: combobox, lbx: listbox
    btn_filter_by_name = Button(newWindow, width = 20, command = FilteringName)
    ent_filter_by_name = Entry(newWindow, width = 15, font = "나눔고딕 -28")
    btn_filter_by_phone_number = Button(newWindow, width = 20, command = FilteringPhoneNumber)
    ent_filter_by_phone_number = Entry(newWindow, width = 15, font = "나눔고딕 -28")
    btn_filter_by_address = Button(newWindow, width = 20, command = FilteringAddress)
    cbx_filter_by_address1 = ttk.Combobox(newWindow, height = 15, values = addressA_tuple, font = "나눔고딕 -28")
    cbx_filter_by_address2 = ttk.Combobox(newWindow, height = 15, values = addressB_tuple, font = "나눔고딕 -28")
    btn_filter_by_stay = Button(newWindow, width = 20, command = FilteringTime)
    cbx_filter_by_time_hour = ttk.Combobox(newWindow, height = 15, values = hour_tuple, font = "나눔고딕 -28")
    cbx_filter_by_time_min = ttk.Combobox(newWindow, height = 15, values = min_tuple, font = "나눔고딕 -28")
    lbx_people = Listbox(newWindow, selectmode = 'extended', height = 0)
    #Widget Place
    btn_filter_by_name.pack()
    ent_filter_by_name.pack()
    btn_filter_by_phone_number.pack()
    ent_filter_by_phone_number.pack()
    btn_filter_by_address.pack()
    cbx_filter_by_address1.pack()
    cbx_filter_by_address2.pack()
    btn_filter_by_stay.pack()
    cbx_filter_by_time_hour.pack()
    cbx_filter_by_time_min.pack()
    lbx_people.pack()
#EndRegion
#Region Loading
def Loading():
    fileName = filedialog.askopenfilename(initaldir = '/', title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    person_strings = LoadFile(fileName)
    for person_string in person_strings:
        toPerson(person_string)
#EndRegion
#Region Saving
def Saving():
    fileName = filedialog.askopenfilename(initaldir = '/', title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    SaveFile(fileName)
#EndRegion
#Region Graph
def ShowGraph():
    bar_graph = CreateBarGraph()
    line_graph = CreateLineGraph()
    circle_graph = CreateCircleGraph()

    def DrawBarGraph(room_list):
        squareA = graph.create_polygon(30, 30, 40, 50, 50, 30, 40, 20, fill = '#04213a', outline = '#ffffff')
    
    def DrawLineGraph(time_zone_list):
        max = time_zone_list[0]
        for time_zone in time_zone_list:
            if max < time_zone:
                max = time_zone
        top = (max // 10 + 1) * 10


    def DrawCircleGraph(age_zone_list):
        new_age_zone = []
        sum_age_people = 0
        for people in age_zone_list:
            sum_age_zone += people
        for age_zone in age_zone_list:
            new_age_zone.append(age_zone / sum_age_zone)

    graph = Canvas(window, relief = "solid", bd = 1, bg = '#ffffff')
    graph.pack()
    #Method
    
#EndRegion
#Region Widget Create
#lbl: label, ent: entry, cbx: combobox, btn: button
lbl_name = Label(window, text = "이름", width = 4, height = 1, font = "나눔고딕 -28", anchor="sw")
ent_name = Entry(window, width = 15, font = "나눔고딕 -28")
lbl_age = Label(window, text = "나이", width = 4, height = 1, font = "나눔고딕 -28", anchor="sw")
cbx_age = ttk.Combobox(window, height = 15, values = age_tuple, font = "나눔고딕 -28")
lbl_gender = Label(window, text = "성별", width = 4, height = 1, font = "나눔고딕 -28", anchor="sw")
cbx_gender = ttk.Combobox(window, height = 15, values = gender_tuple, font = "나눔고딕 -28")
lbl_address = Label(window, text = "주소", width = 4, height = 1, font = "나눔고딕 -28", anchor="sw")
cbx_address1 = ttk.Combobox(window, height = 15, values = addressA_tuple, font = "나눔고딕 -28")
cbx_address2 = ttk.Combobox(window, height = 15, values = addressB_tuple, font = "나눔고딕 -28")
lbl_time_in = Label(window, text = "입장 시간", width = 8, height = 1, font = "나눔고딕 -27", anchor="sw")
cbx_time_in_hour = ttk.Combobox(window, height = 15, values = hour_tuple, font = "나눔고딕 -28")
lbl_cl1 = Label(window, text = ":", width = 4, height = 1, font = "나눔고딕 -28", anchor="center")
cbx_time_in_min = ttk.Combobox(window, height = 15, values = min_tuple, font = "나눔고딕 -28")
lbl_time_out = Label(window, text = "퇴장 시간", width = 8, height = 1, font = "나눔고딕 -27", anchor="sw")
lbl_water = Label(window, text = "~", width = 4, height = 1, font = "나눔고딕 -28", anchor="center")
lbl_cl2 = Label(window, text = ":", width = 4, height = 1, font = "나눔고딕 -28", anchor="center")
cbx_time_out_hour = ttk.Combobox(window, height = 15, values = hour_tuple, font = "나눔고딕 -28")
cbx_time_out_min = ttk.Combobox(window, height = 15, values = min_tuple, font = "나눔고딕 -28")

lbl_phone_number = Label(window, text = "전화번호", width = 8, height = 1, font = "나눔고딕 -28", anchor="sw")
ent_phone_number = Entry(window, width = 15, font = "나눔고딕 -28")
lbl_room_number = Label(window, text = "방 번호", width = 4, height = 1, font = "나눔고딕 -28", anchor="sw")
cbx_room_number = ttk.Combobox(window, height = 15, values = room_tuple, font = "나눔고딕 -28")

btn_register = Button(window, text = "등록하기", font = "나눔고딕 -27",width = 20, command = CheckPhoneNumber)
btn_find = Button(window, text = "대상 찾기", font = "나눔고딕 -27",width = 20, command = Finding)
btn_load = Button(window, text = "불러오기", font = "나눔고딕 -27",width = 20, command = Loading)
btn_save = Button(window, text = "저장하기", font = "나눔고딕 -27",width = 20, command = Saving)
btn_graph = Button(window, text = "그래프로 보여주기", font = "나눔고딕 -27",width = 20, command = ShowGraph)
#EndRegion
#Region Widget Place

#3F
lbl_name.place(x = 50, y = 100, width=100, height=45)
ent_name.place(x = 50, y = 150, width=200, height=50)

lbl_age.place(x = 280, y = 100, width=100, height=45)
cbx_age.place(x = 280, y = 150, width=100, height=50)

lbl_gender.place(x = 410, y = 100, width=100, height=45)
cbx_gender.place(x = 410, y = 150, width=100, height=50)

lbl_address.place(x = 540, y = 100, width=100, height=45)
cbx_address1.place(x = 540, y = 150, width=160, height=50)
cbx_address2.place(x = 710, y = 150, width=160, height=50)

lbl_time_in.place(x = 900, y = 100, width=150, height=45)
cbx_time_in_hour.place(x = 900, y = 150, width=55, height=50)
lbl_cl1.place(x = 955, y = 150, width=10, height=50)
cbx_time_in_min.place(x = 965, y = 150, width=55, height=50)

lbl_water.place(x = 1025, y = 150, width=20, height=50)

lbl_time_out.place(x = 1050, y = 100, width=150, height=45)
cbx_time_out_hour.place(x = 1050, y = 150, width=55, height=50)
lbl_cl2.place(x = 1105, y = 150, width=10, height=50)
cbx_time_out_min.place(x = 1115, y = 150, width=55, height=50)

#2F
lbl_phone_number.place(x = 50, y = 250, width=120, height=45)
ent_phone_number.place(x = 50, y = 300, width=250, height=50)
lbl_room_number.place(x = 330, y = 250, width=100, height=45)
cbx_room_number.place(x = 330, y = 300, width=100, height=50)

btn_register.place(x = 470, y = 275, width=150, height=75)
btn_find.place(x = 650, y = 275, width=150, height=75)
btn_save.place(x = 840, y = 275, width=150, height=75)
btn_load.place(x = 1030, y = 275, width=150, height=75)

#1F
#temp
btn_graph.place(x = 960, y = 250, width=150, height=50)
#EndRegion
window.mainloop()
