#  Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо  energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5
from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, satiety=50, energy=50):
        self.satiety = max(0, min(satiety, 100))
        self.energy = max(0, min(energy, 100))

    # – збільшує  energy до 100
    def sleep(self):
        print("sleep")
        self.energy = 100

    #– їсть, збільшує satiety на food_amount
    def eat(self, food_amont) :
        self.satiety = min(100, self.satiety+food_amont)

    def  play(self, activity_level):
        pass

    def make_sound(self):
        pass

class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy =max(0, self.energy - 2* activity_level)
            self.satiety = max(0, self.satiety -  activity_level)
        print(f" Ситість: {self.satiety}, Енергія: {self.energy}")

    def  make_sound(self):
        print('Мяу')

    def catch_mouse(self):
        if self.energy > 30:
            print('ловить мишу')
        elif self.energy > 40:
            print('грається з мишею')
        else:
            print('їсть')


class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max(0,self.energy- activity_level / 2)
            self.satiety = max(0,self.satiety- activity_level/2)
            print(f" Ситість: {my_cat.satiety}, Енергія: {my_cat.energy}")
        else:
            self.energy = max(0,self.energy- activity_level)
            self.satiety = max(0,self.satiety- activity_level)
            print(f" Ситість: {my_cat.satiety}, Енергія: {my_cat.energy}")

    def  make_sound(self):
        print('Гав')

    def  fetch_ball(self):
        print('ловить м’яча')
        if self.satiety > 10:
            self.energy = max(0, self.energy-5)


cat1 = Cat(20,30)
cat1.make_sound()
cat1.catch_mouse()
cat1.play(20)
cat1.catch_mouse()
cat1.eat(70)
cat1.sleep()

print(f" Ситість: {cat1.satiety}, Енергія: {cat1.energy}")


