import random
import json


def start_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Вгадайте число (від 1 до 100): "))
            attempts += 1
            if guess < number:
                print("Більше!")
            elif guess > number:
                print("Менше!")
            else:
                print(f"Вітаємо! Ви вгадали число {number} за {attempts} спроб.")
                return attempts <= 5
        except ValueError:
            print("Будь ласка, введіть коректне число.")


def save_results(wins, losses):
    with open("results.json", "w") as file:
        json.dump({"wins": wins, "losses": losses}, file)


def load_results():
    try:
        with open("results.json", "r") as file:
            data = json.load(file)
            return data.get("wins", 0), data.get("losses", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, 0


def main():
    wins, losses = load_results()

    while True:
        print("\n1. Почати нову гру\n2. Вивести результат\n3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            if start_game():
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
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
