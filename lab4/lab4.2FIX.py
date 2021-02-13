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
print(ans)