# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
import json
import pickle
music_group = {}



def add_group(band_name1):
    if band_name1 not in music_group:
        music_group[band_name1] = []
    else:
        print("Група вже в списку.")


def add_album(band_name, band_albums):
    if band_name not in music_group:
        add_group(band_name)
    music_group[band_name].extend(band_albums)

def save_pickle(bands, filename='band.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(bands, file)

def save_json(bands, filename='band.json'):
    with open(filename, 'w') as file:
        json.dump(bands, file)

def load_pickle(filename='band.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception:
        print('Невдалось завантажити')
        return {}


def load_json(filename='band.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception:
        print('Невдалось завантажити')
        return {}


def info_band():
    for band in music_group:
        print("Група: ")
        for album in music_group(band):
            print(album)

def main():
    music_group = {}
    while True:
        print('''Виберіть:
                1. Додати групу.
                2. Додати альбом
                3. Зберегти Json
                4. Зберегти Pickle
                5. Завантажити Json
                6. Завантажити Pickle''')

        user_choice = input('Введіть команду: ')

        if user_choice == '1':
            band_name1 = input("Введіть назву групи: ")
            add_group(band_name1)

        elif user_choice == '2':
            band_name = input("Введіть назву групи: ")
            albums = input("Введіть назву альбому (або кілька через кому): ").split(", ")
            add_album(band_name, albums)

        elif user_choice == '3':
            save_json(music_group)
            print("Дані збережено у JSON.")

        elif user_choice == '4':
            save_pickle(music_group)
            print("Дані збережено у Pickle.")

        elif user_choice == '5':
            music_group = load_json()
            print("Дані завантажено з JSON.")

        elif user_choice == '6':
            music_group = load_pickle()
            print("Дані завантажено з Pickle.")
        else:
            break


if __name__ == '__main__':
    main()






groups = {
    "The Beatles": ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"],
    "Queen": ["A Night at the Opera", "News of the World"],
    "Pink Floyd": ["The Dark Side of the Moon", "Wish You Were Here"],
    "Metallica": ["Master of Puppets", "Ride the Lightning"],
    "Nirvana": ["Nevermind", "In Utero"],
    "Led Zeppelin": ["Led Zeppelin IV", "Houses of the Holy"],
    "The Rolling Stones": ["Sticky Fingers", "Exile on Main St."],
    "U2": ["The Joshua Tree", "Achtung Baby"],
    "AC/DC": ["Back in Black", "Highway to Hell"],
    "Coldplay": ["Parachutes", "A Rush of Blood to the Head"]
}
# Завдання 1
# Створіть клас Recipe з атрибутами  name – назва страви
#  ingredients – список продуктів  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item)  – перевіряє чи є інгредієнт в рецепті
#  __gt__(self, other)  – перевіряє чи є час приготування self більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список. Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом приготування, скористайтесь функцією min


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients  # Fixed typo
        self.text = text
        self.time = time

    def __str__(self):
        return f"Назва страви: {self.name}"

    def __contains__(self, item):
        print(f'{item} ')
        return item in self.ingredients  # Fixed typo

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print("-" * 20)
        print(f"Назва страви: \n '{self.name}'")
        print("-" * 20)
        print("Інгредієнти:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}", end=" ")



recipe1 = Recipe("Піца",
       ["борошно", "вода", "дріжджі", "томат", "сир"],
       "Готуємо тісто, додаємо інгредієнти та запікаємо",
       30)

recipe2 = Recipe("Салат",        ["томат", "огірок", "зелень", "олія"],
       "Нарізаємо овочі, додаємо зелень та поливаємо олією ", 10)

recipe3 = Recipe("Суп",        ["вода", "картопля", "морква", "м'ясо"],
       "Варимо всі інгредієнти до готовності",        45)

recipe1.display_info()

print("огірок" in recipe1)
print("----" *5 )
print(min(recipe1, recipe2))
print("+++++" *5 )

recipe1.display_info()
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle

def add_item(items):
    item = input('Введіть назву товару: ')
    items.append(item)


def print_items(items):
    print('Товари: ')
    for item in items:
        print('   ', item)


def save_json(items, filename='items.json'):
    with open(filename, 'w') as file:
        json.dump(items, file)


def save_pickle(items, filename='items.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(items, file)


def load_json(filename='items.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception:
        print('Невдалось завантажити')
        return []



def load_pickle(filename='items.pkl'):
     try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
     except Exception:
        print('Невдалось завантажити')
        return []



def main():
    items = []
    while True:
        print('''Виберіть:
            1. Додати товар.
            2. Вивести список товарів
            3. Зберегти Json
            4. Зберегти Pickle
            5. Завантажити Json
            6. Завантажити Pickle''')

        user_choice = input('Введіть команду: ')

        if user_choice == '1':
            add_item(items)

        elif user_choice == '2':
            print_items(items)

        elif user_choice == '3':
            save_json(items)

        elif user_choice == '4':
            save_pickle(items)

        elif user_choice == '5':
            items = load_json()

        elif user_choice == '6':
            items = load_pickle()

        else:
            break


if __name__ == '__main__':
    main()
#вантажте дані за допомогою pickle та json.