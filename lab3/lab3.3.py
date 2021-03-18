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



