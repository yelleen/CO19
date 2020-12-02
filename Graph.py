from FileIO import Person, people
init_time = 10
def CreateBarGraph():
    global people
    room = [0, 0, 0, 0]
    for person in people:
        room[person.room_number - 1] += 1
    return room
def CreateLineGraph():
    global people, init_time
    time_zone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for person in people:
        person_time = person.timeToList()
        if person_time[0] != person_time[2]:
            time_zone[person_time[2] - init_time] += 1 #if init_time is 10, than person_time[0], person_time[2] is more than 10. min value of person_time[0] - init_time should be same with 0.
        time_zone[person_time[0] - init_time] += 1
        return time_zone
def CreateCircleGraph():
    global people
    age_zone = [0, 0, 0, 0, 0, 0, 0, 0]
    for person in people:
        age_zone[person.age // 10 - 1] += 1 #person.age: 10-80, if person is teenager/twenties, than the index of age_zone would be 0/1.
    return age_zone