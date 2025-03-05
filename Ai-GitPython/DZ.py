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
from abc import ABC, abstractmethod

class Passenger():
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def __str__(self):
        return self.name

class Transport(ABC):
    @abstractmethod
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        time_in_bus = distance / self.speed
        print('Time in travel to ', destination,' =', time_in_bus)

class Bus(Transport):
    def __init__(self,speed, capacity):
        super().__init__(speed)
        self.passengers = []
        self.capacity = capacity

    def board_passenger(self, passenger):
        if len(self.passengers) >= self.capacity:
            print('Bus is full')
        else:
            self.passengers.append(passenger)
            print(passenger, ' is in bus')

    def move(self, destination, distance):
        super().move(destination, distance)
        leaving_pass = []
        left_pass = []
        for p in self.passengers:
            if p.destination == destination:
                leaving_pass.append(p)

            else:
                left_pass.append(p)

        time_in_bus = distance / self.speed

        print(len(leaving_pass), 'passengers leave the bus after ', time_in_bus, ' Hours')
        self.passengers = left_pass



bus1 = Bus(60, 10)
bus1.move('Lviv', 600)
pas1 = Passenger('Ivan', 'Dnipro')
pas2 = Passenger('Yana', 'Lviv')

bus1.board_passenger(pas1)
bus1.board_passenger(pas2)
bus1.move('Lviv', 600)

Time in travel to  Lviv  = 10.0
0 passengers leave the bus after  10.0  Hours
Ivan  is in bus
Yana  is in bus
Time in travel to  Lviv  = 10.0
1 passengers leave the bus after  10.0  Hours

Process finished with exit code 0