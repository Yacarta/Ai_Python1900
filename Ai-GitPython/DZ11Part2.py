#  Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта #  баланс #  валюта #  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).


class Bank:
    exchange_rates = {"usd": 41, "eur": 43, "grn": 1}
    currency_ukr = {"usd": "Доларів", "eur": "Євро", "grn": "Гривень"}

    def __init__(self, name, balans, currency):
        self.name = name
        self.balans = balans
        self.currency = currency
        self.is_currency()

    def is_currency(self):
        if self.currency not in self.exchange_rates:
            raise ValueError(f"Невідома валюта {self.currency}")

    def print_info(self):
        print(f"Шановний {self.name}, у Вас на рахунку {self.balans} {self.currency_ukr[self.currency]}")

    def exchange(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Невідома валюта")

        exchange_amount = amount * self.exchange_rates[from_currency] / self.exchange_rates[to_currency]
        print(
            f"{amount} {self.currency_ukr[from_currency]} по курсу = {exchange_amount:.2f} {self.currency_ukr[to_currency]}")
        return exchange_amount

    #  зміна валюти
    def change_currency(self, currency):
        if currency not in self.exchange_rates:
            raise ValueError("Невідома валюта")
        if currency != self.currency:
            self.balans = self.exchange(self.balans, self.currency, currency)
            self.currency = currency
            print(
                f"Ваш рахунок переведено в {self.currency_ukr[currency]}."
                f" У Вас {self.balans:.2f} {self.currency_ukr[currency]}")

# поповнення балансу(валюта та сама)
    def add_currency(self, amount):
        self.balans += amount
        print(f"Ваш рахунок  поповнено. У Вас {self.balans} {self.currency_ukr[self.currency]} ")

    def withdraw(self, amount):
        if amount <= self.balans:
            self.balans -= amount
            print(f"Ви зняли з рахунку {amount}."
                  f" У Вас залишилося на рахунку {self.balans} {self.currency_ukr[self.currency]} ")
        else:
            print(f"Недостатньо коштів на рахунку. У Вас на рахунку {amount} ")




# зняття грошей з балансу(валюта та сама).


client = Bank("Jhon", 2000, "usd")
client.print_info()
client.exchange(500, 'usd', 'grn')
client.change_currency("grn")
client.add_currency(1000)
client.print_info()
client.withdraw(5000)
client.print_info()

