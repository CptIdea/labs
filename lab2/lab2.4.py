print("======Вариант 1======")
someStr = input("Строка: ")
ans = ''
for cur in someStr:
    if cur.isdigit():
        ans += cur
print(ans)


print("======Вариант 2======")
someStr = input("Строка: ")
ans = ''
for cur in someStr:
    if cur.isalpha():
        ans += cur
print(ans)


print("======Вариант 3======")
someStr = input("Строка: ")
ans = ''
for cur in someStr:
    if cur.isupper():
        ans += 'Л'
    if cur.islower():
        ans += 'л'
print(ans)


print("======Вариант 4======")
someStr = input("Строка: ")
ans1 = ''
ans2 = ''
for cur in someStr:
    if cur.isalpha():
        ans2 += cur
    if cur.isdigit():
        ans1 += cur
print(ans1)
print(ans2)

