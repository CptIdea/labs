f = open("lab5/data/students.csv","r")

students = []

for raw in f.read().splitlines()[1:]:
    splitted =  raw.split(';')
    students.append([splitted[0],splitted[1],splitted[2],splitted[3]])


variant = int(input("Номер варианта?\n>"))

if variant == 1:
    for v in students:
        v[2] = int(v[2])+1


elif variant == 2:  
    for v in students:
        v[2] = int(v[2])-1


elif variant == 3:  
    group = input("Группа?\n>")
    for v in students:
        if group == v[3]:
            v[2] = int(v[2])+1

    
elif variant == 4:  
    group = input("Группа?\n>")
    for v in students:
        if group == v[3]:
            v[2] = int(v[2])-1

print(*students,sep='\n')