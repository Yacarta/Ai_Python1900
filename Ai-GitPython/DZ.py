#  Завдання 1
# Використовуючи класи з практичної реалізуйте клас Shop з
# трьома чергами до кас. Кожна черга реалізується через
# двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги
# номер idx
#  serve_buyer(idx) – обслуговує покупця з черги
# idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить
# в чергу з номером idx
#  display_info() – виводить на екран 3 черги
# Посилання на код
from queue import Queue


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.prev} --> {self.data} --> {self.next}'

class DoubleLinkedList:
    def __init__(self):
        self.head = Node

    def push_end(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self,data):
        new_node = data
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head =new_node


    def pop_end(self):
        if not self.tail:
            return None
        removed_data = self.tail.data
        if self.head == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed_data


    def pop_start(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if self.head == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_data

    def display_info(self):
        buyer =[]
        head = self.head

        while head:
            buyer.append(head)
            head = head.next
        return buyer





class Shop:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.queue3 = Queue()



    def __str__(self):
        return f"{self.data} -> {self.next}"


    def add_buyer(self,name, idx):
        if idx == 1:
            self.queue1(name)
        elif idx == 2:
            self.queue2(name)
        elif idx == 3:
            self.queue3(name)
        else:
            print('Not  queue')







shop = Shop()
shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)
print("Черги:")
# shop. display_info()
# shop.serve_buyer(1)
# shop.serve_buyer(2)
# shop.serve_buyer(3)
# print("Після обслуговування покупців:")
# shop. display_info()
# shop.serve_buyer(1)
# print("Покупці перейшли до вільної каси:")
# shop. display_info()
