# import json
#
#
# data = [1,2,3]
#
# filename = "data.json"
# with open(filename, 'w') as file
#     json.dump


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











# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.