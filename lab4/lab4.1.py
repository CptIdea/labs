matrix = list(
    map(
        lambda x: list
        (map(int,x.split())),
            input("Ввод матрицы.\nДелитель столбцов - ' '\nДелитель строк - ';'\n>").split(';')))

sum = 0
for s in matrix:
    print(s)
for s in matrix:
    for n in s:
        sum+=n
print("Сумма элементов:",sum)