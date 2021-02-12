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
    