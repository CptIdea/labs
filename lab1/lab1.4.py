someList = list(map(int, input("Введите числа: ").split()))
print("======Вариант 1======")
result = someList[0]
for i in someList:
    if i > result:
        result = i
print(result)

print("======Вариант 2======")
result = someList[0]
for i in someList:
    if i < result:
        result = i
print(result)

print("======Вариант 3======")
result = 0
for i in someList:
    result += i
result = result / len(someList)
print(result)

print("======Вариант 4======")
print(someList[len(someList) // 2])
