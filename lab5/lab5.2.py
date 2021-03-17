f = open("lab5/data/students.csv","r")

students = []

for raw in f.read().splitlines()[1:]:
    splitted =  raw.split(';')
    students.append([splitted[0],splitted[1],splitted[2],splitted[3]])


print("=====Вариант 1=====")
students.sort(key = lambda s: s[1])
for s in students:
    print(s)


print("=====Вариант 2=====")
students.sort(key = lambda s: s[2])
for s in students:
    print(s)

print("=====Вариант 3=====")
students.sort(key = lambda s: s[3])
for s in students:
    print(s)

print("=====Вариант 4=====")
for s in students:
    if int(s[2])>22:
        print(s)