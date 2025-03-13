# rate1 = Banking.exchange_rates[from_currency]
# rate2 = Banking.exchange_rates[to_currency]
# return amount * rate1 / rate2

import time
import datetime

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


class Message:
    def __init__(self, text):
        self.text = text
        #self.time = time.time()  # кількість секунд  1970 року
        self.time = datetime.datetime.now().time()  # нинішній чис

    def __str__(self):
        return f"[{self.time}] {self.text}"


# клас для обробки повідомлень
class Messenger:
    def __init__(self):
        self.messages = DoubleLinkedList()

    def add_message(self, text):
        # добавити в кінець черги
        message = Message(text)

        self.messages.push_end(message)

    def read_next_message(self):
        if self.messages.is_empty():
            print('Повідомлень немає')
            return

        # дістає найдавніше повідемлення
        message = self.messages.pop_start()

        print(f"Читаємо повідомлення: {message}")


# m = Messenger()
#
# m.add_message('Hello')
# time.sleep(1) # чекає 1 секунду
# m.add_message("What`s up")
# time.sleep(2) # чекає 2 секунди
# m.add_message("I`m fine")
#
#
# m.read_next_message()
# time.sleep(1)
# m.read_next_message()
# time.sleep(1)
# m.read_next_message()


# list1 = [1, 2, 3, 4]
# list2 = ['a', 'hello']
# list3 = [[1, 2, 3], Node(), ]


# пріоритетна черга
from queue import PriorityQueue


# створення пріоритетної черги
queue = PriorityQueue()

# добавити елемент
symtom = 'болить голова'
priority = 3

data = (priority, symtom)

queue.put(data)

# одним рядком
# queue.put((3, 'болить голова'))
# queue.put((priority, symtom))

# queue.put((3, 'болить горло'))
# queue.put((1, 'струс мозку'))
# queue.put((2, 'просто спитати'))
#
# # дістати елемент
#
# data = queue.get()  # отримуєте пару пріоритет, дані
# print(data)
#
# data = queue.get()  # отримуєте пару пріоритет, дані
# print(data)
#
# data = queue.get()  # отримуєте пару пріоритет, дані
# print(data)
#
# priority, symtom = queue.get()  # отримуєте пару пріоритет, дані
# print(symtom)
#
# print(queue.empty())

# Використовуючи чергу створіть клас FastFoodQueue для
# організації роботи черг у фасфуді. Є 4 каси, новий клієнт стає
# в ту, де найменше людей. Коли клієнт зробив замовлення,
# його добавляють в чергу на отримання. Має зберігатися час,
# коли людина зробила замовлення, та коли отримала
# замовлення. Інформація про час обслуговування має
# зберігатись у окремому списку
# Атрибути:
#  queues – список з 4-ма чергами до кас
#  order_queue – черга клієнтів на отримання замовлення
#  service_duration_history – список з часом обслуговування
# клієнтів
# Методи:
#  add(client) – додає клієнта в найкоротшу чергу
#  serve(idx) – обслуговуємо клієнта з черги за індексом.
# Треба додати клієнта в order_queue разом з часом коли
# зроблено замовлення
#  make_order() – видає готове замовлення клієнту та
# обраховує скільки часу очікував клієнт. Це число треба
# добавити в service_duration_history
#  show_statistics() – виводить мінімальний, максимальний
# та середній час обслуговування клієнтів

# TASK 1
import time


class Client:
    def __init__(self, name):
        self.name = name
        self.time = time.time()


class FastFoodQueue:
    def __init__(self):
        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()
        self.queue4 = DoubleLinkedList()
        self.order_queue = DoubleLinkedList()
        self.queues = [self.queue1, self.queue2, self.queue3, self.queue4]
        self.duration_history = []


    def add(self, name):
        min_queue = min(self.queues)
        min_queue.push_end(name)


    def serve(self, idx):

        serve_client = self.queues[idx].pop_start()
        client = Client(serve_client)
        self.order_queue.push_end(client)

    def make_order(self):
        client = self.order_queue.pop_start()
        now_time = time.time()
        difference = now_time - client.time
        self.duration_history.append(difference)

        print(f"{client.name} receive order after {difference:.0f} sec")


    def show_statistics(self): #виводить мінімальний, максимальний # та середній час обслуговування клієнтів
        min_time = min(self.duration_history)
        max_time = max(self.duration_history)
        ser_time = sum(self.duration_history) / len(self.duration_history)
        print(f'мінімальний {min_time:.0f}  час обслуговування клієнтів')
        print(f'максимальний {max_time:.0f}  час обслуговування клієнтів')
        print(f'середній {ser_time:.0f}  час обслуговування клієнтів')




#
#
#
# # Тестування
# fast_food = FastFoodQueue()
# fast_food.add("Олег")
# fast_food.add("Анна")
# fast_food.add("Марія")
# fast_food.add("Сергій")
#
# fast_food.serve(0)
# fast_food.serve(1)
#
# time.sleep(2)
# fast_food.make_order()
# time.sleep(3)
# fast_food.make_order()
#
# fast_food.show_statistics()

# Завдання 2
# Використовуючи черги з пріоритетом створіть програму
# для симуляції роботи аеропорту. Кожен пасажир має пройти
# через 3 етапи: реєстрація, контроль безпеки, посадка.
# Відповідно аеропорт складається з 3-ох зон, кожна з яких має
# свою чергу. Коли Пасажир пройшов одну зону, то переходить
# в наступну.
# Пасажири з вищим пріоритетом обслуговуються першими
# Клас Zone – зона
# Атрибути:
#  name – назва(реєстрація, контроль безпеки або посадка)
#  passengers – черга пасажирів
# Методи:
#  add(passenger) – додає пацієнта в чергу з пріоритетом
#  serve_passenger() – обслуговуємо наступного пасажира
# та повертає його
# Клас Airport – аеропорт
# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3
# зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги
# реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги
# контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та
# переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній
# зоні та скільки успішно все пройшли
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет

from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Zone:

    # Методи:
    #  add(passenger) – додає пацієнта в чергу з пріоритетом
    #  serve_passenger() – обслуговуємо наступного пасажира
    # та повертає його
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



class Airport:
# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3
# зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги
# реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги
# контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та
# переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній
# зоні та скільки успішно все пройшли
    def __init__(self):
        self.zones = {"Registration": Zone("Реєстрація"),
                      "Control": Zone("Контроль"),
                      "Board": Zone("Посадка")}
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passanger(passenger)

    def serve_registration(self):
        pas = self.zones["Registration"].serve_passenger()
        self.zones["Control"].add_passanger(pas)

    def serve_security_control(self):
        pas = self.zones["Control"].serve_passenger()
        self.zones["Board"].add_passanger(pas)

    def serve_boarding(self):
        pas = self.zones["Board"].serve_passenger()
        self.passengers.append(pas)

    def show_statistics(self):
        print(len(self.passengers))


# Тестування
airport = Airport()
passengers = [
    Passenger("Олег", 3),
    Passenger("Анна", 1),
    Passenger("Марія", 4),
    Passenger("Сергій", 2)
]

for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_security_control()
airport.serve_boarding()

airport.show_statistics()

