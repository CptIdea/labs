matrix = []

while True:
    cur = input('>')
    if cur != '':
        matrix.append(list(map(int,cur.split())))
    else:
        break    

sum = 0
for s in matrix:
    print(s)
for s in matrix:
    for n in s:
        sum+=n
print("Сумма элементов:",sum)