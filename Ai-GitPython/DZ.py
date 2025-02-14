#  Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:
    def __init__(self, client, items):
        self.client = client
        self.items = items


    def add_product(self, product):
        self.items.append(product)
        print(f'Товар "{product}" додано до кошика.')



    def delete_product(self, product1):
        if product1 in self.items:
            self.items.remove(product1)
            print(f'Товар "{product1}" видалено з кошика.')
        else:
            print(f'Товар відсутній у кошику.')


    def print_info(self):
        print(f"Шановний {self.client} у вас в кошику: {self.items}")



# shop1 = Cart("Іван", ["Яблуко", "Черешня"])
# shop1.print_info()
# shop1.add_product("Груша")
# shop1.print_info()


# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.
class Phone:
    def __init__(self, number,batery_level):
        self.number = number
        self.batery_level = batery_level

    def discharge(self, level):


        if self.batery_level < level:
            print(f"Неможливо зменшити на {level}%. ")
        else:
            self.batery_level -= level
            print(f"Заряд зменшено на {level}%")

    def print_info(self):
        print(f"Номер телефону {self.number} має {self.batery_level}% зарядкию")
        if self.batery_level <= 20 and self.batery_level >= 0:
            print(" Ваш телефон потрібно зарядити")

telephone = Phone(38050320, 80)
telephone.print_info()

telephone.discharge(65)
telephone.print_info()