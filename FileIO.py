#Region Class Person
class Person:
    def __init__(self, name, age, gender, phone_number, address1, address2, time_in, time_out, room_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.address1 = address1
        self.address2 = address2
        self.time_in = time_in
        self.time_out = time_out
        self.room_number = room_number
    def toString(self):
        person_string = ""
        person_string += self.name + ' ' + str(self.age) + ' ' + self.gender + ' '
        person_string += self.phone_number + ' ' + self.address1 + ' ' + self.address2 + ' '
        person_string += self.time_in + ' ' + self.time_out + ' ' + self.room_number + '\n'
        return person_string
    def timeToList(self):
        allTime = []
        check_in = self.time_in.split(':')
        check_out = self.time_out.split(':')
        allTime.append(int(check_in[0]))
        allTime.append(int(check_in[1]))
        allTime.append(int(check_out[0]))
        allTime.append(int(check_out[1]))
        return allTime
#EndRegion
#Region Field
lines = []
people = []
#EndRegion
#Region Load File
def LoadFile(fileName):
    global lines
    lines.clear()
    dataFile = open(fileName, 'r')
    lines = dataFile.readlines
    dataFile.close()
    return lines
def toPerson(person_string):
    global people
    person_element = person_string.split(' ')
    person = Person(person_element[0], int(person_element[1]), person_element[2], person_element[3], person_element[4], person_element[5], person_element[6], person_element[7], int(person_element[8]))
    people.append(person)
#EndRegion
#Region Save File
def SaveFile(fileName):
    global people
    dataFile = open(fileName, 'a')
    for p in people:
        p_string = p.toString()
        dataFile.write(p_string)
    people.clear()
    dataFile.close()
#EndRegion