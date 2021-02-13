my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102',['Акулова Алена', 'Бабушкина Ксения']],['БО-331103',['Акулова Алена', 'Бабушкина Ксения']]]

groups = {}
for cur in my_len:
    groups[cur[0]]=cur[1]

i = 0
for g in groups:
    print("{}){}".format(i,g))
    i+=1

i = int(input("Выберите группу > "))

while i>=len(groups) or i<0:
    i = int(input("Выберите существующую группу > "))

print("======Вариант 1======")
print(list(groups)[i])
for student in groups[list(groups)[i]]:
    print(student)
print()

print("======Вариант 2======")
print(list(groups)[i],end=': ')
for student in groups[list(groups)[i]]:
    print(student,end=', ')
print()
print()

print("======Вариант 3======")
for i in range(len(groups)):
    print(list(groups)[i])
    for student in groups[list(groups)[i]]:
        print(student)
    print()

print("======Вариант 4======")
for i in range(len(groups)):
    print(list(groups)[i],end=': ')
    for student in groups[list(groups)[i]]:
        print(student,end=', ')
    print()
