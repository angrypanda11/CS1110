#DeMarcus Cousins


def myFind(s, t):
    count = 0
    ps = 0
    pt = 0
    ans = 0

    while count != len(s) - 1 and pt != len(t):
        if s[ps] != t[pt]:
            ans += 1
            ps += 1
            count += 1

        else:
            ps += 1
            pt += 1
            count += 1

    if pt != len(t):
        return -1
    else:
        return ans

print(myFind("divided", "ide"))


def mysplit(s):
    s = str(s)
    s_2 = []
    blk = ""
    for i in s:
        if i == " ":
            s_2.append(blk)
            blk = ""
        else:
            blk += i
    if blk:
        s_2.append(blk)

    if s[-1] == " ":
        s_2.append(blk)

    return s_2

print(mysplit("   "))
print(mysplit('a string divided'))
print(mysplit(' divided'))
print(mysplit(' divided '))
print(mysplit('   ')) # there are 3 spaces here

print(mysplit("Child soldiers cheap labor alcoholism and that place that has all the rice"))
print(mysplit("filthy cockroaches and thieving wee gypsies and that place got fucking nuked twice"))
# print(mysplit("hit-men on scooters and edgy school shooters the one where the president's a cuck"))
# print(mysplit("the one that is sunny the one with no money and one that is completely fucked"))
# print(mysplit("muslims and muslims and muslims and muslims and also that place with the jews"))
# print(mysplit("all of the slavs that removed the kebabs and ONE THAT CANT POO IN THE LOO"))