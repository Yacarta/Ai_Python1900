
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







