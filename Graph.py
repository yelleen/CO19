from FileIO import FuncTime

initTime = 10

def CreateBarGraph(personList):
    room = [0, 0, 0, 0]
    for p in personList:
        room[p.roomNumber - 1] += 1
    return room

def CreateLineGraph(personList):
    global initTime
    timeZone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for p in personList:
        timeList = FuncTime(p)
        if timeList[0] != timeList[2]:
            timeZone[timeList[2] - initTime] += 1 #if initTime is 10, than timeList[0], timeList[2] is more than 10. min value of timeList[0] - initTime should be same with 0.
        timeZone[timeList[0] - initTime] += 1
    return timeZone

def CreateCircleGraph(personList):
    ageZone = [0, 0, 0, 0, 0, 0, 0, 0]
    for p in personList:
        ageZone[p.age // 10 - 1] += 1 # p.age: 10~80, if p is teenager/twenties, than the index of ageZone would be 0/1.
    return ageZone