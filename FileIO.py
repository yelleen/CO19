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


def read():
    people_list = []
    people_txt = open("people.txt","r")
    lines = people_txt.readlines
    i = 0
    for line in lines:
        per_list[] = line.split(' ')
        list_name = "person" + i
        list_name = Person(per_list[0], per_list[1], per_list[2], per_list[3], per_list[4], per_list[5], per_list[6], per_list[7], per_list[8])
        people_list.append(list_name)
        i += 1
        

def timeKnow(person):
    timeList = [] 
    people_list = open("people.txt","r")
    line = person_list.readline

def TimeSet(person):
    time = []
    return time # 시간, 분, 시간, 분

def FuncTime(p):
    t = [1,1,1,1]
    return t
