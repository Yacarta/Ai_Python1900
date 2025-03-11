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



class Shop:
    def __init__(self):
        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()
        self.count = [0,0,0]

    def get_queue(self, idx):
        if idx ==1:
            return self.queue1
        elif idx == 2:
            return self.queue2
        elif idx == 3:
            return self.queue3


  #  def __str__(self):
    #    return f"{self.data} -> {self.next}"


    def add_buyer(self,name, idx):
        queue = self.get_queue(idx)
        queue.push_end(name)
        self.count[idx -1] += 1



    def serve_buyer(self, idx): # обслуговує покупця з черги
        queue = self.get_queue(idx)



        # if queue.head is None:
        #     self._reorder(idx)

        buyer = queue.pop_start()
        self.count[idx - 1] -= 1
        print(buyer, 'покупець обслуговується з черги ' , idx)
        if queue.head is None:
            self._reorder(idx)

    def _reorder(self, idx):
        """
        Якщо черга порожня, бере покупця з max черги.
        """

        index_max_queue = self.count.index(max(self.count))
        if self.count[index_max_queue] == 0:
            print("Немає покупців для перенесення.")
            return
        max_queue = self.get_queue(index_max_queue +1)
        change_buyer = max_queue.pop_end()              # name from max queue
        self.add_buyer(change_buyer, idx)               #add
        self.count[index_max_queue] -=1




    def display_info(self):
        print('Черга 1: ', self.queue1)
        print('Черга 2: ', self.queue2)
        print('Черга 3: ', self.queue3)
        print(self.count)


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
shop. display_info()
shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)
print("Після обслуговування покупців:")
shop. display_info()
shop.serve_buyer(1)
print("Покупці перейшли до вільної каси:")
shop. display_info()

shop. display_info()
shop.serve_buyer(1)
shop. display_info()
shop.serve_buyer(1)
shop. display_info()

Черги:
Черга 1:  Олег -> Ірина -> None
Черга 2:  Марина -> Марія -> Василь -> None
Черга 3:  Андрій -> Тетяна -> Сергій -> Анна -> None
[2, 3, 4]
Олег покупець обслуговується з черги  1
Марина покупець обслуговується з черги  2
Андрій покупець обслуговується з черги  3
Після обслуговування покупців:
Черга 1:  Ірина -> None
Черга 2:  Марія -> Василь -> None
Черга 3:  Тетяна -> Сергій -> Анна -> None
[1, 2, 3]
Ірина покупець обслуговується з черги  1
Покупці перейшли до вільної каси:
Черга 1:  Анна -> None
Черга 2:  Марія -> Василь -> None
Черга 3:  Тетяна -> Сергій -> None
[1, 2, 2]
Черга 1:  Анна -> None
Черга 2:  Марія -> Василь -> None
Черга 3:  Тетяна -> Сергій -> None
[1, 2, 2]
Анна покупець обслуговується з черги  1
Черга 1:  Василь -> None
Черга 2:  Марія -> None
Черга 3:  Тетяна -> Сергій -> None
[1, 1, 2]
Василь покупець обслуговується з черги  1
Черга 1:  Сергій -> None
Черга 2:  Марія -> None
Черга 3:  Тетяна -> None
[1, 1, 1]