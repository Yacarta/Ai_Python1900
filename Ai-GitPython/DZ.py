# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями
import json
import random

def load_game(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def new_game():
    load_game(filename= "new.json")
    win = 0
    lost = 0
    print('Нова гра')
    atempts = 0
    secret_num = random.randint(1, 100)
    print("Вгадайте число від 1 до 100 з 5 спроб")
    while True:
        user_num = input('Введіть ваше число: ')
        if atempts <=5:
            if user_num > secret_num:
                print("Число загадане менше")
            elif user_num < secret_num:
                print("Число загадане більше")
            else:
                atempts += 1
                print(f'Вітаємо!!!!Ви вгадали з {atempts}-ї спроби ')
                win += 1
                return
        else:
            print("Нажаль ви програли :-(")
            lost +=1
            return







def save_game(filename):
    data = {"wins": win, "losses": lost}
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_game(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


def results():
    print(f"Перемог: {win}, Поразок: {lost}")

def main():
    while True:
        print("\n1. Почати нову гру\n2. Вивести результат\n3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            if new_game():
                wins += 1
                print("Ви перемогли!")
            else:
                losses += 1
                print("Переміг комп'ютер!")
            save_results(wins, losses)
        elif choice == "2":
            print(f"Перемог: {wins}, Поразок: {losses}")
        elif choice == "3":
            break