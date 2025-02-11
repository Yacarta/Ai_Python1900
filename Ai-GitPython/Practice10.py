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


student1 = Student('Sergiy', 32)
student2 = Student('vict', 32)
student3 = Student('roy', 32)
student1.print_info()
student2.print_info()
student3.print_info()