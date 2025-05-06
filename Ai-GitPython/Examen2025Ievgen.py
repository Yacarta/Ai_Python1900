import random


#  Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

user_number1 = int(input('Введіть перше число: '))
user_number2 = int(input('Введіть друге число: '))

if user_number1 > user_number2:
    user_number1, user_number2 = user_number2, user_number1

sum_num = 0
for i in range(user_number1, user_number2+1):
    sum_num += i

print(f'Cумa діапазону чисел між {user_number1} і {user_number2} дорівнює {sum_num}')

Напишіть програму, для знаходження суми всіх парних
чисел від 1 до 100.

sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print('Сумма всіх парних чисел= ', sum)

# Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

user_text = input(" Введіть слово: ")
for i in user_text:
    print(i, end="\n")

# Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

numbers = []
for i in range(20):
    random_num = random.randint(1,20)
    numbers.append(random_num)
print(numbers)
number_odd = []
for i in numbers:
    if i % 2 == 0:
        number_odd.append(i)
print(number_odd)

# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

def text_cap(text):
    final_text = []
    for i in text:
        i = i.strip()
        if i  and i[0].isupper():
            final_text.append(i)
    return final_text



text = input("Введіть текст з рядками через кому: ").split(',')
result = text_cap(text)
print(result)

Напишіть функцію, яка приймає список рядків від
користувача і повертає новий список, що містить лише
рядки, які містять слово "Python".

def text_cap(text):
    final_text = []
    for i in text:
        i = i.strip()
        if "Python" in i:
            final_text.append(i)
    return final_text

text = input("Введіть текст з рядками через кому: ").split(',')
result = text_cap(text)
for line in result:
    print(line)

Напишіть програму, яка
створює словник, де ключами є слова, а значеннями - їхні
визначення. Дозвольте користувачу додавати, видаляти
та шукати слова у цьому словнику
dict = {}
def add_dict():
    word = input("Введіть слово: ")
    definition = input("Введіть визначення: ")
    dict[word] = definition
    print(f"Слово '{word}' додано.")

def dell_word(word):
    if word in dict:
        dict.pop(word)

def search_word(word):
    if word in dict:
        print(f"{word}: {dict[word]}")

while True:
    print("1 - додавати")
    print("2 - видаляти")
    print("3 - шукати слова")
    print("4 - Вийти")

    command = input('Введіть номер команди: ')

    if command == '1':
        add_dict()
    elif command == '2':
        word = input('Введіть слово для видалення')
        dell_word(цщкв)
    elif command == '3':
        word = input('Введіть слово для пошуку')
        search_word(word)
    elif command == '4':
        print("Вихід з програми.")
        break
    else:
        print('невірна команда')




 #  Симулятор роботи сайту
#  WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
#  Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
#  WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.

# class Webpage:
#     def __init__(self, title, content, publication_date):
#         self.title = title
#         self.content = content
#         self.publication_date = publication_date
#
#     def display_details(self):
#         print(f"Заголовок: {self.title}")
#         print(f"Вміст: {self.content}")
#         print(f"Дата публікації: {self.publication_date}")
#
# class Website:
#     def __init__(self, name, web_url):
#         self.name = name
#         self.web_url = web_url
#         self.list_page = []
#
#     def add_page(self, title):
#         self.list_page.append(title)
#         print("Сторінка додана успішно.")
#
#     def remove_page(self, title):
#         for page in self.list_page:
#             if page.title == title:
#                 self.list_page.remove(page)
#                 print(f"Сторінка '{title}' видалена.")
#                 return
#         print(f"Сторінку '{title}' не знайдено.")
#
#     def display_info(self):
#         print(f"\nНазва сайту: {self.name}")
#         print(f"URL: {self.web_url}")
#         print("Сторінки:")
#
#         if not self.list_page:
#             print("  Сторінок немає.")
#         for page in self.list_page:
#             print("--------------")
#             page.display_details()
#
# def main():
#     while True:
#         print("Меню:")
#         print("1 - створення сайту")
#         print("2 - додавання сторінок")
#         print("3 - видалення сторінок")
#         print("4 -  відображення  інформації про сайт")
#         print("5 -  Вихід з програми")
#
#
#
#         command = input('Введіть номер команди: ')
#
#         if command == '1':
#             name = input("Введіть назву сайту: ")
#             web_url = input("Введіть URL сайту: ")
#             website = Website(name, web_url)
#             print("Сайт створено успішно.")
#         elif command == '2':
#             title = input("Введіть заголовок сторінки: ")
#             content = input("Введіть вміст сторінки: ")
#             publication_date = input("Введіть дату публікації: ")
#             page = Webpage(title, content, publication_date)
#             website.add_page(page)
#         elif command == '3':
#             title = input("Введіть заголовок сторінки для видалення: ")
#             website.remove_page(title)
#         elif command == '4':
#             website.display_info()
#         elif command == '5':
#             print("Вихід з програми.")
#             break
#         else:
#             print('невірна команда')
#
# if __name__ == "__main__":
#     main()