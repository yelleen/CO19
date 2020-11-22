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
    people_list = open("people.txt","r")
    line = person_list.readline

def TimeSet(person):
    time = []
    return time # 시간, 분, 시간, 분

def FuncTime(p):
    t = [1,1,1,1]
    return t
