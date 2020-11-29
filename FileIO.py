import os
from GUI_yelleen import fileName
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

def AddPersonToFile(fileName, pList): # in order to write file and add person
    dataFile = open(fileName, 'a')
    for p in pList:
        pStr = p.toString()
        dataFile.write(pStr)
    dataFile.close()

def ReadText(fileName):
    peopleStr = open(fileName, 'r')
    lines = peopleStr.readlines
    peopleStr.close()
    return lines

def StringToPerson(pstr, pList):
    pe = pstr.split(' ')
    p = Person(pe[0], pe[1], pe[2], pe[3], pe[4], pe[5], pe[6], pe[7], pe[8])
    pList.append(p)

def TimeSet(person):
    time = []
    time_in = person.time_in
    time_out = person.time_out

    check_in = time_in.split(':')#추출한 문자열을 나눠서 time 배열에 int형으로 추가하기
    time.append(int(check_in[0]))
    time.append(int(check_in[1]))

    check_out = time_out.split(':')
    time.append(int(check_out[0]))
    time.append(int(check_out[1]))

    return time # 시간, 분, 시간, 분

def name_check(name,people_list):#이름 중복 체크
    people_list = ReadText(fileName)
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
    people_list = ReadText(fileName)
    person_class = people_list[index]
    return person_class.phone_number

def PersonClass(index):#해당자의 class 반환
    people_list = ReadText(fileName)
    return people_list[index]
