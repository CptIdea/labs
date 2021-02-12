someList = list(input("Введите список: ").split())

print("======Вариант 1======")
for i in someList:
    if 5<len(i)<10:
        print(i)

print("======Вариант 2======")
for i in someList:
    if len(i)<10:
        print(i)

print("======Вариант 3======")
for i in someList:
    if i[-1]=='r':
        print(i)

print("======Вариант 4======")
for i in someList:
    if i[0]=='r':
        print(i)