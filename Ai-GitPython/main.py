# OOP

# def move(self, destination, distance):
#     leaving_passengers = []
#     left_passengers = []
#
#     for p in self.passengers:
#         if p.destination == destination:
#             leaving_passengers.append(p)
#         else:
#             left_passengers.append(p)
#
#     self.passengers = left_passengers
#
# a + b  # __add__
# a > b  # __gt__
# num in nums  # __contains__

# структури даних

# нотація O

# n = 10
# a = 2 + 3  # швидкість не залежить від n. O(1)
#
#
# for i in range(n):  # кількість операцій залежить від n. O(n)
#     print(i)
#
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)
#
# for i in range(n):     # O(n^2)
#     for j in range(n):
#         print(i+j)

# import math
#
# N = 10**12
# print(math.log(N))


# зв'язний список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # вузол який йде наступним

    def __str__(self):
        return f"{self.data} -> {self.next}"


# node1 = Node(4)
# node2 = Node('abc')
# node3 = Node(5)
#
# node1.next = node2
# node2.next = node3
#
# print(node1)


class LinkedList:
    def __init__(self):
        self.head = None  # перший вузол, поки що список порожній

    def append(self, data):
        node = Node(data)

        # якщо список пустий
        if self.head is None:
            self.head = node
            return  # кінець

        # знайти останній вузол
        end = self.head

        while end.next is not None:  # поки можна рухатись далі
            end = end.next

        end.next = node

    def __str__(self):
        return str(self.head)


class LinkedList1:
    def __init__(self):
        self.head = None  # перший вузол, поки що список порожній
        self.tail = None  # останній вузол, поки що список порожній

    def append(self, data):
        node = Node(data)

        # якщо список пустий
        if self.head is None:
            self.head = node
            self.tail = node
            return  # кінець

        # добавити в кінець вузол
        self.tail.next = node
        self.tail = node

    def __str__(self):
        return str(self.head)


# list1 = LinkedList1()
#
# list1.append(2)
# list1.append(5)
# list1.append(1)
# list1.append(4)

# print(list1)
# Створіть клас однозв’язного списку SinglyLinkedList
# Методи
#  print() – виводить список на екран
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_start() – видалити перший елемент

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} -> {self.next}"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return f"{self.head}"

    def push_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node



# data = SinglyLinkedList()
# data.push_end(1)
# data.push_end(2)
# data.push_end(3)
# print(data)

    def push_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def pop_start(self):
        if self.head is None:
            raise ValueError('List is empty')

        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        # self.head = self.head.next
        next_node = self.head.next
        self.head.next = None
        self.head = next_node




#
# data = SinglyLinkedList()
# data.push_end(10)
# data.push_end(2)
# data.push_end(3)
# data.push_start(5)
# print(data)
# data.pop_start()
# print(data)

# Створіть клас двозв’язного списку DoubleLinkedList
# Методи
#  print(reversed=False) – виводить список на екран(з
# початку або з кінця залежно від reversed)
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_end() – видалити останній елемент
#  pop_start() – видалити перший елемент

nums = [0,1,4]
print(max(nums))
print(nums)
nums[1] +=1
print(nums)
ind = nums.index(max(nums))
print(ind)