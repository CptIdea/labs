someList = list(input("Введите список: ").split())

print("=======Вариант 1:=======")
for i in range(0, len(someList)):
    if i % 2 == 0:
        print(someList[i])

print("=======Вариант 2:=======")
for i in range(0, len(someList)):
    if i % 2 == 1:
        print(someList[i])

print("=======Вариант 3:=======")
for i in range(0, len(someList)):
    if i % 2 == 0:
        print(someList[i],end=' ')
print("\n=======Вариант 4:=======")
for i in range(0, len(someList)):
    if i % 2 == 1:
        print(someList[i],end=' ')