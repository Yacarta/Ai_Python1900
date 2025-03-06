# class Shop:
#     def __init__(self):
#         self.queue1 = DoublyLinkedList()
#         self.queue2 = DoublyLinkedList()
#         self.queue3 = DoublyLinkedList()
#
#     def get_queue(self, idx):
#         if idx == 1:
#             return self.queue1
#         elif idx == 2:
#             return self.queue2
#         elif idx == 3:
#             return self.queue3
#
#
#     def add(self, name, idx):
#         queue = self.get_queue(idx)
#         queue.push_end(name)

class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def __str__(self):
        return f"{self.name} - {self.destination}"

    def __repr__(self):
        return f"{self.name} - {self.destination}"


# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        print(f"До місця {destination} їхали {distance // self.speed} годин.")


# list1 = []
# list1[2]  # O(N) -- кількість операцій співрадає(в середньому) з кількітю елементів у списку
# list1[::-1]  # задом наперед O(N)
# list1 += [1, 2, 3]  # O(N)
# list1.append(2)  # O(N)

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

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
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



# stack = DoubleLinkedList()
# print(stack)
#
# stack.push_end(2)  # добавити до стеку
# print(stack)
#
# stack.push_end(4)
# stack.push_end(1)
# stack.push_end(5)
# print(stack)
#
#
# last_num = stack.pop_end()
# print(f"{last_num=}")
# print(stack)

# є послідовність символів, видалити дублікати,
# які знаходяться пору

# abbbccccaaaabbb -> abcab

text = "abbbccccaaaabbb"
stack = DoubleLinkedList()

for char in text:
    # якщо стек порожній
    # print(stack)
    if stack.is_empty():
        stack.push_end(char)
        continue  # переходимо до наступної літери

    # last_char = stack.pop_end()  # дістаємо останню
    #
    # if last_char == char:
    #     # вертаємо last_char назад
    #     stack.push_end(last_char)
    # else:
    #     stack.push_end(last_char)
    #     stack.push_end(char)


    # з peek
    last_char = stack.peek()

    if last_char != char:
        stack.push_end(char)


# перевести стек в str
new_text = ''

while not stack.is_empty():
    last_char = stack.pop_end()
    new_text = last_char + new_text

#print(new_text)
# авдання 2
# Використовуючи стек створіть клас EnterNumber для
# введення числа в рядку
# Атрибути:
#  digits – стек з введеними цифрами
# Методи:
#  add(digit) – додати нову цифру, вивести помилку якщо
# не цифра
#  undo() – видалити останню цифру
#  get_number() – повернути число
#  clear() – очистити стек

class EnterNumber:
    def __init__(self):
        self.digits = DoubleLinkedList()

    def add_didg(self, digit):
        self.digits.push_end(digit)

    def undo(self):
        self.digits.pop_end()

    def get_number(self):
        num_str = ''

        while not self.digits.is_empty():
            if self.digits.peek().isdigit():
                num_str = self.digits.pop_end() + num_str
            else:
                raise ValueError("In text not only digit. Operation is break.")

        return int(num_str)

    def clear(self):
        self.digits = DoubleLinkedList()



# reader = EnterNumber()
# dig = input("Enter the digit: ")
# reader.add_didg(dig)
# dig = input("Enter the digit: ")
# reader.add_didg(dig)
# dig = input("Enter the digit: ")
# reader.add_didg(dig)
#
# reader.clear()
#
# dig = input("Enter the digit: ")
# reader.add_didg(dig)
#
#
# print(reader.get_number())
# # print()
#
# авдання 1
# Використовуючи стек створіть клас WebHistory
# Атрибути:
#  history – стек з історією відвідування веб сторінок
#  forward_history – стек з веб сторінками, для повернення
# «вперед»
# Методи:
#  add(page) – перейти на нову сторінку
#  undo() – повернутись на попередню сторінку
#  redo() – перейти вперед
#  get_current_page() – повернути поточну сторінку
class WebHistory:
    def __init__(self):
        self.history = DoubleLinkedList()
        self.forward_history = DoubleLinkedList()

    def add(self, page):
        self.history.push_end(page)
        self.forward_history = DoubleLinkedList()

    def undo(self):
        page = self.history.pop_end()
        self.forward_history.push_end(page)

    def redo(self):
        redo_page = self.forward_history.pop_end()
        self.history.push_end(redo_page)


    def get_current_page(self):
        return self.history.peek()

# Є вираз з дужками, за допомогою стеків визначіть чи
# правильно розтавлені дужки, якщо ні то виведіть індекс
# «проблемної» дужки.
# def highlight_character(text, ind):
#     for i, char in enumerate(text, start=1):
#         if i == ind:
#             print(f"\033[91m{char}\033[0m", end="")
#         else:
#             print(char, end="")
#     print()
#
#
# text = "2+(3*[5+6])/{(1+5+7)-(1+[-8])}"
#
# stack = DoubleLinkedList()
#
# is_correct = True
#
# for char in text:
#     if char in "([{":
#         stack.push_end(char)
#     elif char in ")]}":
#         if stack.is_empty():
#             is_correct = False
#             break
#
#         last_char = stack.pop_end()
#
#         if last_char + char in ["()", '[]', '{}']:
#             is_correct = True
#         else:
#             is_correct = False
#             break
#
# if not stack.is_empty():
#     is_correct = False
#
#
# print(is_correct)
#
#
# highlight_character(text, 10)