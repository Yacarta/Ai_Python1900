#class dog

#опис класу

class Dog:
    name = 'Monty'
    age = 2
    weight =5

    #можливість гавкати

    def make_sound(self):
        print('Gav')

dog1  = Dog()

print(dog1.name)
print(dog1.age)



#використання метода

dog1.make_sound()