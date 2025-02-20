# nums = [1, 4, 5, 2]
# a = 1
# b = 2
#
# a == b
# a.__eq__(b)
#
# a + b
# a.__add__(b)
#
# a > b
# a.__gt__(b)
#
# 3 in nums
# nums.__contains__(3)
#
# nums[2]
# nums.__getitem__(2)
#
# nums.append
#
# min max sort

#  Створіть клас Cart з атрибутами
#  items – список товарів
#  total – загальна ціна товарів
# методи:
#  __str__(self) – повертає рядок зі списком товарів
#  __len__(self) – повертає кількість товарів
#  __add__(self, other) – об’єднує 2 кошики та повертає
# новий кошик
# Створіть два кошики. Виведіть кількість товарів в кожному
# з них. Виведіть самі кошики. Об’єднайте їх та виведіть
# кількість товарів в новому кошику та товари в ньом


class Cart:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def __str__(self):
        text = ''
        for item in self.items:
            text += str(item) + ', '

        text = text[:-2]
        return f"{text}. Загальна ціна {self.total}$"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_items = self.items + other.items
        new_total = self.total + other.total
        new_cart = Cart(new_items, new_total)
        return new_cart

    def __gt__(self, other):  # self > other
        return len(self) > len(other)

    def __lt__(self, other): # self < other
        return not (self > other)

    def __eq__(self, other): # self == other
        return (set(self.items), self.total) == (set(other.items), other.total)
        #return  self.items == other.items and self.total == other.total

    def __contains__(self, item): # item in self
        return item in self.items

    def __getitem__(self, idx): # self[idx]
        return self.items[idx]

    def __iter__(self):  # for item in self
        #return iter(self.items)
        for item in self.items:
            yield item

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

# генератор квадратів чисел

# def square_range(finish):
#     for num in range(finish):
#         yield num**2
#
#
# for num in square_range(5):  # yield
#     print(num)
#
# num = square_range(5)  # return
# a = 1
# b = 2
#
# c = a + b
#

cart1 = Cart(['TV', 'laptop'], 170)
cart2 = Cart(['phone'], 65)

cart3 = Cart(['laptop', 'TV'], 170)

# print(cart1 == cart3)

#
# print(cart1)
# text = str(cart2)
# print(text)
#
# print(f"Кошик1: кількість товарів: {len(cart1)}")
#
# cart3 = cart1 + cart2
# print(cart3)
# print(f"Кошик3: кількість товарів: {len(cart3)}")
#
# if cart3 > cart2:
#     print('Кошик 3 більший')
#
#
# max_cart = max(cart1, cart2)
# print(max_cart)
#
#
# carts = [cart3, cart2, cart1]
# print()
# print()
# print('кошики до сортування')
# for cart in carts:
#     print(cart)
#
# carts.sort()
# print()
# print()
# print('кошики після сортування')
# for cart in carts:
#     print(cart)
#
# print()
# print()
#
# print("Apple" in cart1)
# print("TV" in cart1)
# print("Apple" not in cart1)
#
# print()
# print()
#
# second_item = cart3[1]
# print(second_item)
#
# print()
# print()
#
# for item in cart3:  # iter(cart3)
#     print(item)

# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self)  – повертає довжину повідомлення
#  __gt__(self, other)  – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть
from  datetime import datetime
class Message:
    def __init__(self, user, text, str_time):
        self.user = user
        self.text = text
        self.time = datetime.strptime(str_time, '%H:%M')

    def __str__(self):
        str_time = datetime.strftime(self.time, '%H:%M')
        return f"{str_time}--{self.text}--{self.user}"

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        return self.time > other.time




message1 = Message("Bob", "Hello", "20:00")
message2 = Message("Marry", "How are you", "20:01")
message3 = Message("Bob", "Hello", "20:00")
# print(message1)
# print(len(message1))
# print(message1 > message3)
#
# messages = [message3, message1, message2]
# for mess in messages:
#     print(mess)
# messages.sort()
# for mess in messages:
#     print(mess)


# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#   __len__(self)  – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран

class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Song):
            return (self.author, self.name) == (other.author, other.name)
        else:
            return False

    def __str__(self):
        return f"{self.author} пісня '{self.name}'"


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        for song in self.songs:
            yield song

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

song1 = Song("Imagine", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Shape of You", "Ed Sheeran")
song4 = Song("Imagine", "John Lennon")

playlist = Playlist([])
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
print(len(playlist))
print(song4 in playlist)
playlist.remove_song(song4)

for song in playlist:
    print(song)

    print(song)