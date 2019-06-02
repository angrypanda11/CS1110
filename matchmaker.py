

def agreement(i1, i2):
    list_of_things = []
    for i in range(len(i1)):
        if i1[i] in i2:
            list_of_things.append(i1[i])
    return list_of_things


def disagreement(i1, i2):
    list_of_things_2 = []
    for i in range(len(i1)):
        if i1[i] not in i2:
            list_of_things_2.append(i1[i])
    for i in range(len(i2)):
        if i2[i] not in i1:
            list_of_things_2.append(i2[i])
    return list_of_things_2


def compatibility(i1, i2):
    return len(agreement(i1, i2))/(len(agreement(i1, i2)) + len(disagreement(i1, i2)))


def bestmatch(me, others):
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility(me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom
