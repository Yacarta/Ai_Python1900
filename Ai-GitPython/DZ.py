#  Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

import threading

numbers = []

def user_num():
    while True:
        try:
            user_input1 = input('Enter first number (or press Enter to exit): ')
            if user_input1 == '':
                break
            user_num1 = int(user_input1)
            numbers.append(user_num1)

            user_input2 = input('Enter second number (or press Enter to exit): ')
            if user_input2 == '':
                break
            user_num2 = int(user_input2)
            numbers.append(user_num2)



        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    print(numbers)


def sum_number(numbers):
    print(sum(numbers))

def seredne(numbers):
    if len(numbers) ==0:
        print("Список пустий")
    else:
        print(sum(numbers)/len(numbers))


def sum_num(num_list):
    resu = sum(num_list)
    print(resu)


thread1 = threading.Thread(target=user_num)
thread1.start()
thread1.join()
thread2 = threading.Thread(target=sum_number, args=(numbers,))
thread3 = threading.Thread(target=seredne, args=(numbers,))
thread2.start()
thread3.start()
thread2.join()
thread3.join()



