#class dog

#опис класу

class Dog:
    #constructor
    def __init__(self, name, age, weight):
        self.name = name
        self.age =age
        if age < 0:
            raise ValueError('Age must be >0')
        self.weight = weight


    # name = 'Monty'
    # age = 2
    # weight =5

    #можливість гавкати

    def make_sound(self):
        print('Gav')

    def print_info(self):
        print(self.name, self.age, self.weight)


dog1  = Dog(name='Lev', age=3, weight=5)


print(dog1.name)

dog1.print_info()



#використання метода

dog1.make_sound()