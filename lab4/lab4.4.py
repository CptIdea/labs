class student(object):
    def __init__(self, name, surname, group,nom):
        self.name = name
        self.surname = surname
        self.group = group
        self.nom = nom
    
  
my_len  =  [['БО-331101',['Акулова  Алена',  'Бабушкина Ксения','Павленко Антон']],['БОВ-421102',['Васильев Игорь','Митрохин Валерий']],['БО-331103',['Джавадян Армен','Горный Илья','Антонов Антон']]]

students = []

for raw in my_len:
    group = raw[0]
    i=1
    for rawStudent in raw[1]:
        rawName = rawStudent.split()
        students.append(student(rawName[1],rawName[0],group,i))
        i+=1

print("======Вариант 1======")
for student in students:
    if student.surname[0]=='А':
        print(student.surname,student.name,student.group)

print("======Вариант 2======")
for student in students:
    if len(student.surname)<7:
        print(student.surname,student.name,student.group)

print("======Вариант 3======")
for student in students:
    if student.surname[0]=='П' and student.name[0]=='А':
        print(student.surname,student.name,student.group)

print("======Вариант 4======")
for student in students:
    if student.nom % 2 == 0:
        print(student.surname,student.name,student.group)