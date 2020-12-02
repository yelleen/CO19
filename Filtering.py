from FileIO import Person, people

def FilterByName(name):
    global people
    filtered_people = []
    for person in people:
        if person.name == name:
            filtered_people.append(person)
    return filtered_people
def FilterByPhoneNumber(phone_number):
    global people
    filtered_people = []
    for person in people:
        if person.phone_number == phone_number:
            filtered_people.append(person)
    return filtered_people
def FilterByAddress(address):
    global people
    filtered_people = []
    for person in people:
        if person.address1 == address[0] and person.address2 == address[1]:
            filtered_people.append(person)
    return filtered_people
def FilterByStay(time):
    global people
    filtered_people = []
    for person in people:
        person_time = person.timeToList()
        if person_time[0] <= time[0] and person_time[1] <= time[1]:
            if (person_time[2] > time[0]) or (person_time[2] == time[0] and person_time[3] >= time[1]):
                filtered_people.append(person)
    return filtered_people