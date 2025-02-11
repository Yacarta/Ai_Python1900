# #class dog
#
# #опис класу
#
# class Dog:
#     #constructor
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age =age
#         if age < 0:
#             raise ValueError('Age must be >0')
#         self.weight = weight
#
#
#     # name = 'Monty'
#     # age = 2
#     # weight =5
#
#     #можливість гавкати
#
#     def make_sound(self):
#         print('Gav')
#
#     def print_info(self):
#         print(self.name, self.age, self.weight)
#
#     def rename(self, new_name):
#         self.name = new_name
#
#
#
# dog1  = Dog('Lev', 3, 5)
#
#
# print(dog1.name)
#
# dog1.print_info()
#
# dog1.rename("Petr")
# dog1.print_info()
#
# #використання метода
#
# dog1.make_sound()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def print_info(self):
        print(f'Імя: {self.name}, вік: {self.age}')
        print()


# student1 = Student('Sergiy', 32)
# student2 = Student('vict', 32)
# student3 = Student('roy', 32)
# student1.print_info()
# student2.print_info()
# student3.print_info()
# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.
#
# students = []
# for i in range(3):
#     name = input('Імя')
#     age = int(input('Age'))
#
#     student = Student(name, age)
#     students.append(student)
#
# for student in students:
#     student.print_info()
# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius ** 2
#
#     circle1 = Circle(2)
#
#     area1 = circle1.get_area()
#
#     print(area1)
# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостатньо коштів")


    def print_info(self):
        print(f'Власник: {self.owner} на рахунку {self.balance}')


acount = BankAccount('Tom', 2000)
acount.print_info()
acount.deposit(500)
acount.print_info()
acount.withdraw(3000)
acount.print_info()



# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.