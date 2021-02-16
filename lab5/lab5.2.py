class student(object):
    def __init__(self, name, group,nom,age):
        self.name = name
    
        self.group = group
        self.nom = nom
        self.age = age

f = open("lab5/data/students.csv","r")

students = []

for raw in f.read().splitlines()[1:]:
    splitted =  raw.split(';')
    students.append(student(splitted[1],splitted[3],splitted[0],splitted[2]))

for s in students:
    print(s.group)
