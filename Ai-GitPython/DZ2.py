import json
import random

# Global counters for wins and losses
wins = 0
losses = 0

def load_game(filename):
    """Load the game results from the file."""
    global wins, losses
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            wins = data.get("wins", 0)
            losses = data.get("losses", 0)
    except FileNotFoundError:
        # If file doesn't exist, initialize the game
        print("No saved game data found, starting fresh.")
        wins, losses = 0, 0


def save_game(filename):
    """Save the game results to the file."""
    with open(filename, 'w') as file:
        json.dump({"wins": wins, "losses": losses}, file)


def new_game():
    """Start a new game."""
    global wins, losses
    attempts = 0
    secret_num = random.randint(1, 100)
    print("Вгадайте число від 1 до 100 з 5 спроб")

    while attempts < 5:
        user_input = input(f"Введіть ваше число (спроба {attempts + 1}): ")
        try:
            user_num = int(user_input)
        except ValueError:
            print("Будь ласка, введіть дійсне число!")
            continue

        attempts += 1
        if user_num > secret_num:
            print("Число загадане менше")
        elif user_num < secret_num:
            print("Число загадане більше")
        else:
            print(f'Вітаємо!!!! Ви вгадали з {attempts}-ї спроби.')
            wins += 1
            return

    print("Нажаль ви програли :-(")
    losses += 1


def results():
    """Display the current results."""
    print(f"Перемог: {wins}, Поразок: {losses}")


def main():
    load_game('game_data.json')

    while True:
        print("\n1. Почати нову гру\n2. Вивести результат\n3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            new_game()
            save_game('game_data.json')
        elif choice == "2":
            results()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()

