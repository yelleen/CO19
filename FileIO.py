import os
class Person:
    def __init__(self, name, age, gender, phone_number, address1, address2, time_in, time_out, roomNumber):
        self.name = name
        self.age = age #int
        self.gender = gender
        self.phone_number = phone_number
        self.address1 = address1
        self.address2 = address2
        self.time_in = time_in #string "##:##" -> time_in.split(':') -> ##, ##
        self.time_out = time_out
        self.roomNumber = roomNumber #int
    def toString(self): # in order to add person in file by string
        personStr = self.name + ' ' + str(self.age) + ' ' + self.gender + ' ' + self.phone_number + ' ' + self.address1 + ' ' + self.address2 + ' ' + self.time_in + ' ' + self.time_out + ' ' + self.roomNumber + '\n'
        return personStr

def AddPersonToFile(fileName, person): # in order to write file and add person
    dataPath = "Data/" + fileName + ".txt"
    dataFile = open(dataPath, 'a')
    dataStr = person.toString()
    dataFile.write(dataStr)
    dataFile.close()


def ReadTxt():
    people_list = []
    people_txt = open("people.txt","r")
    lines = people_txt.readlines
    i = 0
    for line in lines:
        per_list = line.split(' ')
        list_name = "people" + i
        list_name = Person(per_list[0], per_list[1], per_list[2], per_list[3], per_list[4], per_list[5], per_list[6], per_list[7], per_list[8])
        people_list.append(list_name)
        i += 1
    people_txt.close()
    return people_list

def TimeSet(person_name):
    time = []
    people_list = ReadTxt() #people배열의 획득 방법 토론(1. 인수에서 받기 2. 함수를 호출) 
    time_in = " "
    time_out = " "
    for i in people_list:#해당 이름의 in/out시간을 문자열로 추출
        if person_name == i.name:
            time_in = i.time_in
            time_out = i.time_out

    check_in = time_in.split(':')#추출한 문자열을 나눠서 time 배열에 int형으로 추가하기
    time.append(int(check_in[0]))
    time.append(int(check_in[1]))

    check_out = time_out.split(':')
    time.append(int(check_out[0]))
    time.append(int(check_out[1]))

    return time # 시간, 분, 시간, 분

def name_check(name):#이름 중복 체크
    people_list = ReadTxt()
    check = []
    index = 0
    for i in people_list:
        if i.name == name:
            check.append(index)
        index += 1
    if len(check) > 1:
        return check
    else:
        return check.pop(0)

def phone_num(index):#해당자의 전화번호(문자열) 출력
    people_list = ReadTxt()
    person_class = people_list[index]
    return person_class.phone_number

def PersonClass(index):#해당자의 class 반환
    people_list = ReadTxt()
    return people_list[index]