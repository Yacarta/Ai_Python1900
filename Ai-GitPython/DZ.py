#  Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує
# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали
# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()
from abc import ABC

class Passenger(ABC):
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

class Transport():
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        pass

class Bus():
    def __init__(self, passengers, capacity):
        pass

    def board_passenger(self, passenger):
        pass

    def move(self, destination, distance):
        pass
