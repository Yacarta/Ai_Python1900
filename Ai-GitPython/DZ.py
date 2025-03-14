class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        return str(self.head)

    def __gt__(self, other):
        return self.count > other.count

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        self.count += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        self.count += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.tail:
            return None

        self.count -= 1
        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None


        self.count -= 1
        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def is_empty(self):
        """
        Чи є порожній
        :return: True якщо порожній
        """
        return self.head is None

    def peek(self):
        """
        Повертає останній елемент, не видаляючи його
        :return: останній елемент
        """
        return self.tail.data
# Створіть дочірні класи від Zone та перевизначте метод
# serve_passenger() щоб він повертав пару: пасажир та True/False
# в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету(у багажі)
#  безпека – відсутність небезпечних предметів у багажі:
# ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
#  baggage – список з предметами в багажі
from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add_passanger(self, passenger):
        priority = passenger.priority
        pair = (priority, passenger)
        self.passengers.put(pair)

    def serve_passenger(self):
        priority, passenger = self.passengers.get()
        return passenger

class RegistrationZone(Zone):
    # def registration(self):
    #     docs = ["ticket"]
    #     priority, passenger = self.passengers.get()
    #     doc = docs and passenger.baggage
    #     return passenger, doc

    def registration(self):
        if not self.passengers.empty():
            passenger = self.serve_passenger()
            docs = ["ticket"]
            has_ticket = "ticket" in docs  # Placeholder logic
            return passenger, has_ticket
        return None, False


class SecurityZone(Zone):
    # def serve_passenger(self):
    #     if not self.passengers.empty():
    #         priority, passenger = self.passengers.get()
    #         danger = ["knife", "gun", "explosives"]
    #         return passenger,  not (danger and passenger.baggage)
    #     return None, False
    def serve_passenger(self):
        if not self.passengers.empty():
            passenger = super().serve_passenger()
            danger_items = ["knife", "gun", "explosives"]
            is_safe = not any(item in passenger.baggage for item in danger_items)
            return passenger, is_safe
        return None, False


class Airport:

    def __init__(self):
        self.zones = {"Registration": Zone("Реєстрація"),
                      "Control": Zone("Контроль"),
                      "Board": Zone("Посадка")}
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passanger(passenger)


    def serve_registration(self):
        # docs = ["ticket"]
        # if "ticket" is in docs:
        #     pas = self.zones["Registration"].serve_passenger()
        #     self.zones["Control"].add_passanger(pas)
        # else:
        #     print(f'Cannot register {passenger} because NO {docs}')
        passenger, has_ticket = self.zones["Registration"].registration()
        if passenger and has_ticket:
            self.zones["Control"].add_passenger(passenger)
        else:
            print(f'Cannot register {passenger.name} due to missing ticket.')

    def serve_security_control(self):
        # danger = ["knife", "gun", "explosives"]
        # pas = self.zones["Control"].serve_passenger()
        # self.pass
        # self.zones["Board"].add_passanger(pas)
        passenger, is_safe = self.zones["Control"].serve_passenger()
        if passenger and is_safe:
            self.zones["Board"].add_passenger(passenger)
        else:
            print(f'{passenger.name} failed security check due to prohibited items.')

    def serve_boarding(self):
        pas = self.zones["Board"].serve_passenger()
        self.passengers.append(pas)

    def show_statistics(self):
        print(len(self.passengers))





# Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
for _ in range(10):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()