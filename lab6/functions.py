def lab1_1():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    k = int(input("k: "))
    d = int(input("d: "))
    f = int(input("f: "))


    if a==0 or b==0 or (a + b + c * (k - a / b**3))==0:
        var1 = "zero division"
    else:
        var1 = abs(((a**2 / b**2) + (c**2 * a**2)) / (a + b + c * (k - a / b**3)) + c + (k/b - k/a)*c)


    if a==0 or b==0:
        var2 = "zero division"
    else:
        var2 = abs(((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3)) - (k / b - k / a) * c)**3 - 20000)

    if (c-a)==0:
        var3 = "zero division"
    else:
        var3 = abs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a))

    if a==0:
        var4 = "zero division"
    else:
        var4 = abs(a - b * c * d**3 + (c**5 - a**2)/a + f**3 * (a - 213))


    print(var1,var2,var3,var4,sep='\n')

def lab1_2():
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


def lab1_3():
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


def lab1_4():
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


def lab2_1():
    my_number = 5

    print("=====Вариант 1=====")
    user_number = int(input("Num: "))
    while user_number>=my_number:
        user_number = int(input("Num: "))
    print("Amazing!")


    print("=====Вариант 2=====")
    user_number = int(input("Num: "))
    while user_number!=my_number:
        user_number = int(input("Num: "))
    print("Amazing!")


    print("=====Вариант 3=====")
    user_number = int(input("Num: "))
    while user_number==my_number:
        user_number = int(input("Num: "))
    print("Amazing!")


    print("=====Вариант 4=====")
    user_number = int(input("Num: "))
    while user_number<=my_number:
        user_number = int(input("Num: "))
    print("Amazing!")


def lab2_2():
    someList = list(input("Введите список: ").split())

    print("======Вариант 1======")
    for i in someList:
        if 5<len(i)<10:
            print(i)

    print("======Вариант 2======")
    for i in someList:
        if len(i)<10:
            print(i)

    print("======Вариант 3======")
    for i in someList:
        if i[-1]=='r':
            print(i)

    print("======Вариант 4======")
    for i in someList:
        if i[0]=='r':
            print(i)


def lab2_3():
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


def lab2_4():
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


def lab3_1():
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


def lab3_2():
    class student(object):
        def __init__(self, name, surname, patronym, age, category):
            self.name = name
            self.surname = surname
            self.patronym = patronym
            self.age = age
            self.category = category

    my_string    =    'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'

    data = list(map(lambda x: x.split(';'),my_string.split('_')))[1:]
    students = []
    for s in data:
        students.append(student(s[1],s[0],s[2],s[3],s[4]))


    print("======Вариант 1======")
    print("ФИО\t\t\tКатегория\tВозраст")
    for s in students:
        print("{0} {1} {2}\t{3}\t{4}".format(s.surname,s.name,s.patronym,s.category,s.age))


    print("======Вариант 2======")
    print("ФИО\t\t\tВозраст\tКатегория")
    for s in students:
        print("{0} {1} {2}\t{3}\t{4}".format(s.surname,s.name,s.patronym,s.age,s.category))

    print("======Вариант 3======")
    print("Ф\tИ\tО\t\t\tО студенте")
    for s in students:
        print("{0}\t{1}\t{2}\t{3}, {4}".format(s.surname,s.name,s.patronym,s.category,s.age))


    print("======Вариант 4======")
    print("ФИО\t\t\tО студенте")
    for s in students:
        print("{0} {1} {2}\t{3}, {4}".format(s.surname,s.name,s.patronym,s.category,s.age))


def lab3_3():
    class student(object):
        def __init__(self, name, surname, patronym, age, category):
            self.name = name
            self.surname = surname
            self.patronym = patronym
            self.age = age
            self.category = category


    def sepName(name):
        return name.split(' ')

        my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса"

        data = list(map(lambda x: x.split(';'),my_string.split('_')))[1:]
        students = []
        for s in data:
            s[0] = sepName(s[0])
            students.append(student(s[0][1],s[0][0],s[0][2],s[1],s[2]))

        print("======Вариант 1======")
        print("{:10}\t{:10}\t{:10}\t{:15}\t\t{:15}".format("Фамилия","Имя","Отчество","Категория","Возраст"))
        for s in students:
            if s.surname == 'Петров':
                print("{0:10}\t{1:10}\t{2:10}\t{3:15}\t\t{4:10}".format(s.surname,s.name,s.patronym,s.category,s.age))

        print("======Вариант 2======")
        print("{:10}\t{:10}\t{:10}\t{:15}\t\t{:15}".format("Фамилия","Имя","Отчество","Категория","Возраст"))
        for s in students:
            if s.age == '21 год':
                print("{0:10}\t{1:10}\t{2:10}\t{3:15}\t\t{4:10}".format(s.surname,s.name,s.patronym,s.category,s.age))

        print("======Вариант 3======")
        print("{:10}\t{:10}\t{:10}\t{:15}\t\t{:15}".format("Фамилия","Имя","Отчество","Категория","Возраст"))
        for s in students:
            if s.age > '21 год':
                print("{0:10}\t{1:10}\t{2:10}\t{3:15}\t\t{4:10}".format(s.surname,s.name,s.patronym,s.category,s.age))

        print("======Вариант 4======")
        print("{:10}\t{:10}\t{:10}\t{:15}\t\t{:15}".format("Фамилия","Имя","Отчество","Категория","Возраст"))
        for s in students:
            if s.surname[0]=='А' or s.surname[0]=='Б':
                print("{0:10}\t{1:10}\t{2:10}\t{3:15}\t\t{4:10}".format(s.surname,s.name,s.patronym,s.category,s.age))


def lab3_4():
    my_string = input("Введите строкy")
    print('Слова\tСимволы\n{}\t{}'.format(len(my_string.split()),len(my_string.replace(' ',''))))


def lab4_1():
    matrix = list(
        map(
            lambda x: list
            (map(int,x.split())),
                input("Ввод матрицы.\nДелитель столбцов - ' '\nДелитель строк - ';'\n>").split(';')))

    sum = 0
    print(matrix)
    for s in matrix:
        for n in s:
            sum+=n
    print("Сумма элементов:",sum)


def lab4_2():
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


def lab4_3():
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102',['Акулова Алена', 'Бабушкина Ксения']],['БО-331103',['Акулова Алена', 'Бабушкина Ксения']]]

    groups = {}
    for cur in my_len:
        groups[cur[0]]=cur[1]

    i = 0
    for g in groups:
        print("{}){}".format(i,g))
        i+=1

    i = int(input("Выберите группу > "))

    while i>=len(groups) or i<0:
        i = int(input("Выберите существующую группу > "))

    print("======Вариант 1======")
    print(list(groups)[i])
    for student in groups[list(groups)[i]]:
        print(student)
    print()

    print("======Вариант 2======")
    print(list(groups)[i],end=': ')
    for student in groups[list(groups)[i]]:
        print(student,end=', ')
    print()
    print()

    print("======Вариант 3======")
    for i in range(len(groups)):
        print(list(groups)[i])
        for student in groups[list(groups)[i]]:
            print(student)
        print()

    print("======Вариант 4======")
    for i in range(len(groups)):
        print(list(groups)[i],end=': ')
        for student in groups[list(groups)[i]]:
            print(student,end=', ')
        print()


def lab4_4():
    class student(object):
        def __init__(self, name, surname, group,nom):
            self.name = name
            self.surname = surname
            self.group = group
            self.nom = nom
        
    
    my_len  =  [['БО-331101',['Акулова  Алена',  'Бабушкина Ксения','Павленко Антон']],['БОВ-421102',['Васильев Игорь','Митрохин Валерий']],['БО-331103',['Джавадян Армен','Горный Илья','Антонов Антон']]]

    students = []

    for raw in my_len:
        group = raw[0]
        i=1
        for rawStudent in raw[1]:
            rawName = rawStudent.split()
            students.append(student(rawName[1],rawName[0],group,i))
            i+=1

    print("======Вариант 1======")
    for student in students:
        if student.surname[0]=='А':
            print(student.surname,student.name,student.group)

    print("======Вариант 2======")
    for student in students:
        if len(student.surname)<7:
            print(student.surname,student.name,student.group)

    print("======Вариант 3======")
    for student in students:
        if student.surname[0]=='П' and student.name[0]=='А':
            print(student.surname,student.name,student.group)

    print("======Вариант 4======")
    for student in students:
        if student.nom % 2 == 0:
            print(student.surname,student.name,student.group)


def lab5_1():
    import os
    print(len(os.listdir(input("Dir? "))))


def lab5_2():
    f = open("lab5/data/students.csv","r")

    students = []

    for raw in f.read().splitlines()[1:]:
        splitted =  raw.split(';')
        students.append([splitted[0],splitted[1],splitted[2],splitted[3]])


    print("=====Вариант 1=====")
    students.sort(key = lambda s: s[1])
    for s in students:
        print(s)


    print("=====Вариант 2=====")
    students.sort(key = lambda s: s[2])
    for s in students:
        print(s)

    print("=====Вариант 3=====")
    students.sort(key = lambda s: s[3])
    for s in students:
        print(s)

    print("=====Вариант 4=====")
    for s in students:
        if int(s[2])>22:
            print(s)


def lab5_3():
    f = open("lab5/data/students.csv","r")

    students = []

    for raw in f.read().splitlines()[1:]:
        splitted =  raw.split(';')
        students.append([splitted[0],splitted[1],splitted[2],splitted[3]])


    variant = int(input("Номер варианта?\n>"))

    if variant == 1:
        for v in students:
            v[2] = int(v[2])+1

        print(students)

    elif variant == 2:  
        for v in students:
            v[2] = int(v[2])-1

        print(students)

    elif variant == 3:  
        group = input("Группа?\n>")
        for v in students:
            if group == v[3]:
                v[2] = int(v[2])+1

        print(students)
        
    elif variant == 4:  
        group = input("Группа?\n>")
        for v in students:
            if group == v[3]:
                v[2] = int(v[2])-1

        print(students)

def lab5_4():
    f = open("lab5/data/students.csv","r")

    students = []

    for raw in f.read().splitlines()[1:]:
        splitted =  raw.split(';')
        students.append([splitted[0],splitted[1],splitted[2],splitted[3]])

    f.close()

    variant = int(input("Номер варианта?\n>"))

    if variant == 1:
        for v in students:
            v[2] = int(v[2])+1

        print(students)

    elif variant == 2:  
        for v in students:
            v[2] = int(v[2])-1

        print(students)

    elif variant == 3:  
        group = input("Группа?\n>")
        for v in students:
            if group == v[3]:
                v[2] = int(v[2])+1

        print(students)
        
    elif variant == 4:  
        group = input("Группа?\n>")
        for v in students:
            if group == v[3]:
                v[2] = int(v[2])-1

        print(students)

    ans = input("Сохранить в файл? Y/N\n>")
    if ans == "Y" or ans == "y":
        f = open("lab5/data/students.csv","w")
        raw = "No;ФИО;Возраст;Группа\n"
        for s in students:
            for v in s:
                raw+=str(v)
                raw+=';'
            raw+='\n'
        f.write(raw)


allfunctions = [
    [lab1_1,lab1_2,lab1_3,lab1_4],
    [lab2_1,lab2_2,lab2_3,lab2_4],
    [lab3_1,lab3_2,lab3_3,lab3_4],
    [lab4_1,lab4_2,lab4_3,lab4_4],
    [lab5_1,lab5_2,lab5_3,lab5_4]
    ]