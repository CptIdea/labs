arr = input("List? ").split()

print("======Вариант 1======")
ans = arr[2:]
ans += ['raz',2]
print(ans)

print("======Вариант 2======")
ans = []
for i in range(len(arr)):
    if i % 2 == 0:
        ans += arr[i]
ans += ['raz',2]
print(ans)

print("======Вариант 3======")
if len(arr)<9:
    ans = "Список короче восьми элементов :("
else:
    ans = arr[3:8]
    ans += ['raz',2]
print(ans)

print("======Вариант 4======")
ans = []
ans += ['raz',2,3,4,5]
for i in range(len(arr)):
    if i % 2 == 0:
        ans += arr[i]
print(ans)