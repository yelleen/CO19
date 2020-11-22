from FileIO import Person, FuncTime

def FilterByName(name, personList): # name: string_format"ddd", personList: list
    __people = []
    for p in personList:
        if p.name == name:
            __people.append(p)
    return __people

def FilterByPhoneNumber(phoneNumber, personList): # phoneNumber: string_format"010-####-####", personList: list
    __people = []
    for p in personList:
        if p.phoneNumber == phoneNumber:
            __people.append(p)
    return __people

def FilterByAddress(adr, personList): # name: adr_format"ddd ddd", personList: list
    __people = []
    for p in personList:
        padr = p.address1 + ' ' + p.address2
        if padr == adr:
            __people.append(p)
    return __people

def FilterByStay(time, personList): # tiem: list_size: 2, personList: list
    __people = []
    for p in personList:
        timeList = FuncTime(p)
        if timeList[0] <= time[0] and timeList[1] <= time[1]:
            if (timeList[2] > time[0]) or (timeList[2] == time[0] and timeList[3] >= time[1]):
                __people.append(p)
    return __people


people = []

personA = Person("AAA", 19, "male", "010-1234-5678", "ADR1", "ADR2", "12:30", "13:00", 1)
personB = Person("BBB", 20, "male", "010-2234-5678", "ADR1", "ADR2", "12:30", "13:00", 1)
personC = Person("AAA", 21, "female", "010-1334-5678", "ADR1", "ADR2", "12:30", "13:00", 1)
personD = Person("DDD", 22, "female", "010-1244-5678", "ADR1", "ADR2", "12:30", "13:00", 1)

people.append(personA)
people.append(personB)
people.append(personC)
people.append(personD)

peopleName = FilterByName("AAA", people)

for p in peopleName:
    print(p.age)
    print(p.gender)