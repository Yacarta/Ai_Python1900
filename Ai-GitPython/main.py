# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, data):
#         node = Node(data)
#
#         if self.root is None:
#             self.root = node
#             return
#
#         self._recursive_add(self.root, node)
#
#     def _recursive_add(self, tree_node, added_node):
#         if added_node.data < tree_node.data:
#             # рухаємося наліво
#
#             # перевіряємо чи пусто зліва
#             if tree_node.left is None:
#                 tree_node.left = added_node
#                 return  # рекурсія(цикл) закінчується
#
#             # якщо не пусто
#             self._recursive_add(tree_node.left, added_node)
#         else:
#             # рухаємося направо
#
#             # перевіряємо чи пусто справа
#             if tree_node.right is None:
#                 tree_node.right = added_node
#                 return  # рекурсія(цикл) закінчується
#
#             # якщо не пусто
#             self._recursive_add(tree_node.right, added_node)
#
#     def display(self):
#         nodes_to_display = [self.root]
#
#         while len(nodes_to_display) != 0:
#             # відображаємо все що є в nodes_to_display
#             for node in nodes_to_display:
#                 print(node.data, end=' ')
#             print()
#
#             # отримуємо наступні вузли
#             new_nodes = []
#             for node in nodes_to_display:
#                 if node.left is not None:
#                     new_nodes.append(node.left)
#
#                 if node.right is not None:
#                     new_nodes.append(node.right)
#
#             # замінюємо nodes_to_display на нові вузли
#             nodes_to_display = new_nodes
#
#     def get_min(self):
#         # отримати найменший елемент
#
#         node = self.root
#
#         while node.left is not None:
#             node = node.left
#
#         return node.data
#
#     def find(self, num):
#         # якщо num в корені
#         if self.root.data == num:
#             return True
#
#         return self._recursive_find(self.root, num)
#
#     def _recursive_find(self, tree_node, num):
#         # числа нема
#         if tree_node is None:
#             return False
#
#         # число знайдене
#         if tree_node.data == num:
#             return True
#
#         if num < tree_node.data:
#             return self._recursive_find(tree_node.left, num)
#         else:
#             return self._recursive_find(tree_node.right, num)
#
#
# tree = BinaryTree()
# tree.add(5)
# tree.add(4)
# tree.add(6)
# tree.add(3)
# tree.add(2)
# tree.add(1)
# tree.add(0)
# # tree.display()
# print(tree.get_min())
# print(tree.find(1))
# print(tree.find(10))

import bintrees

class Node:
    def __init__(self, data):
        self.key = data  # вирішуємо наліво чи направо
        self.value = None # додаткова інформація
        self.left = None
        self.right = None


tree = bintrees.AVLTree()

tree.insert(key=10, value='apple')
tree.insert(key=11, value='orange')
tree.insert(key=5, value='pear')
tree.insert(key=9, value='melon')
tree.insert(key=20, value='banana')


# дістати елемент з id 5
print(tree[5])

# ключі str
#
# tree = bintrees.AVLTree()
#
# tree.insert(key='apple', value='sweet juicy apple ')
# tree.insert(key='orange', value='orange')
# tree.insert(key='pear', value='pear')
# tree.insert(key='melon', value='melon')
# tree.insert(key='banana', value='banana')
#
# print(tree['apple'])
#  Завдання 1
# Використовуючи бінарні дерева організуйте роботу
# бібліотеки. В дереві мають зберігатись книжки, відсортовані
# за назвою. Кожного разу коли користувач просить якусь
# книгу, інформація про це зберігається.
# Клас Book
# Атрибути:
#  title – назва книги
#  author – ім’я автор
#  year – рік написання
#  is_returned – чи повернув попередній користувач
#  history – історія користування у вигляді словника де
# ключ це ім’я людини, а значення – True/False в
# залежності чи повернули книгу до бібліотеки
# Клас Library
# Атрибути:
#  books – дерево з книгами
# Методи:
#  add(book) – добавити книгу
#  remove(title) – видалити книгу
#  search(title) – пошук книги за назвою, якщо є то
# повертає книгу інакше None
#  __len__() – кількість книг в бібліотеці
#  borrow_book(client, title) – дати книгу клієнту, якщо
# книга є в бібліотеці та її повернув попередній
# користувач.
# Якщо все добре, то внести всі необхідні зміни в
# інформацію про книгу
#  return_book(client, title) – повернення книги назад в
# бібліотеку
#  display_info(title) – вивести інформацію про книгу,
# включно з історією користування

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_returned = True
        self.history = {}


class Library:
    def __init__(self):
        self.books = bintrees.AVLTree()

    def add(self, book):
        self.books.insert(key=book.title, value=book)

    def remove(self, title):
        if title in self.books:
            self.books.remove(title)
        else:
            print(f'Книжки "{title}" немає!')

    def search(self, title):
        if title in self.books:
            return self.books[title]
        else:
            return

    def __len__(self):
        return len(self.books)

    def borrow_book(self, client, title):
        book = self.search(title)
        if not book:
            print(f'Книжки "{title}" немає!')
            return

        if not book.is_returned:
            print(f'Книжку "{title}" не повернули!')
            return

        print(f'Клієнт {client} забрав з собою книжку')
        book.is_returned = False
        book.history[client] = False

    def return_book(self, client, title):
        book = self.search(title)
        book.is_returned = True
        book.history[client] = True

    def display_info(self, title):
        book = self.search(title)
        print(f'''
Книга - {book.title}
Автор - {book.author}
Рік написання - {book.year}
Історія:''')

        for client, is_ret in book.history.items():
            if is_ret:
                print(f'\tКлієнт {client} повернув книгу')
            else:
                print(f'\tКлієнт {client} не повернув книгу')



library = Library()
books = [
    Book("1984", "Джордж Орвелл", 1949),
    Book("451° за Фаренгейтом", "Рей Бредбері", 1953),
    Book("Преступление и наказание", "Федор Достоевский", 1866),
    Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", 1997),
    Book("Майстер і Маргарита", "Михайло Булгаков", 1966),
    Book("Війна і мир", "Лев Толстой", 1869),
    Book("Гордість і упередження", "Джейн Остін", 1813),
    Book("Злочинний роман", "Агата Крісті", 1920),
    Book("Тарас Бульба", "Микола Гоголь", 1835),
    Book("Собор Паризької Богоматері", "Віктор Гюго", 1831)
]

for book in books:
    library.add(book)

# print(f"📚 У бібліотеці {len(library)} книг.")
#
# library.borrow_book("Олександр", "1984")
# library.borrow_book("Марія", "Гаррі Поттер і філософський камінь")
# library.borrow_book("Андрій", "Війна і мир")
#
# library.return_book("Олександр", "1984")
# library.return_book("Марія", "Гаррі Поттер і філософський камінь")
# library.borrow_book("Андрій", "Гаррі Поттер і філософський камінь")
#
# library.display_info("1984")
# library.display_info("Гаррі Поттер і філософський камінь")
# library.display_info("Війна і мир")

# Створіть програму роботи зі словником. Наприклад,
# англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
#  надавати початкове введення даних для словника
#  відображати слово та його переклади
#  дозволяти додавати, змінювати, видаляти переклади
# слова

from bintrees import AVLTree


class Word:
    def __init__(self, name, translation):
        self.name = name
        self.translations = [translation]


class Dict:
    def __init__(self):
        self.tree_words = AVLTree()

    def add_word(self, name, translation):
        if name in self.tree_words:
            word = self.tree_words[name]
            word.translations.append(translation)
        else:
            new_word = Word(name, translation)
            self.tree_words.insert(name, new_word)

    def get(self, name):
        return self.tree_words[name]


my_dict = Dict()
my_dict.add_word("run", "бігати")
my_dict.add_word("run", "робити")
run = my_dict.get("run")
print(run.translations)