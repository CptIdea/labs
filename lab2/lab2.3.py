import random

print("======Вариант 1======")
lib = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
ans = ''
for _ in range(5):
    ans += lib[random.randint(0,len(lib)-1)]
print(ans)

print("======Вариант 2======")
N = int(input("R: "))
print('R'*N)

print("======Вариант 3======")
lib = '1234567890'
ans = ''
n = random.randint(0,6)
for i in range(6):
    if i != n:
        ans += lib[random.randint(0,len(lib)-1)]
    else:
        ans += '3'
print(ans)

print("======Вариант 4======")
lib = '1234567890йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
dig = '1234567890'
ans = ''
n = random.randint(0,6)
for i in range(8):
    if i != n:
        ans += lib[random.randint(0,len(lib)-1)]
    else:
        ans += dig[random.randint(0,len(dig)-1)]
print(ans)