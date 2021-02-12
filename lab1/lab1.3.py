someList = list(map(int, input("Введите числа: ").split()))

print("======Вариант 1======")
result = 0
for i in someList:
    if i > 10:
        result += i
print(result)

print("======Вариант 2======")
result = 0
for i in someList:
    if 10 > i > 1:
        result += i
print(result)

print("======Вариант 3======")
result = 1
for i in someList:
    if i < 10:
        result *= i
print(result)

print("======Вариант 4======")
result = 1
for i in someList:
    if i < 10:
        result *= i
print(result)