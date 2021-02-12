text = list(input("Текст: ").split())

print("======Вариант 1======")
ans = ''

for cur in text:
    if len(cur)>5:
        ans += cur+' '
print(ans)


print("======Вариант 2======")
ans = ''

for cur in text:
    if cur[:2]=='Ли':
        ans += cur+' '
print(ans)


print("======Вариант 3======")
ans = ''

for cur in text:
    if 5<len(cur)<10:
        ans += cur+' '
print(ans)


print("======Вариант 4======")
ans = ''

for cur in text:
    if cur[-2:]=='ов':
        ans += cur+' '
print(ans)


