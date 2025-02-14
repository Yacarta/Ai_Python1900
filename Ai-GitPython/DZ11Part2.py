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
        exchange_rates = {"usd": 41, "eur": 43, "grn": 1}
        if self.currency not in exchange_rates:
            raise ValueError(f"Невідома валюта{self.currency}")

    def print_info(self):
        currency_ukr = {"usd": "Доларів", "eur": "Євро", "grn": "Гривень"}
        print(f"Шановний {self.name}, у Вас на рахунку {self.balans} {currency_ukr[self.currency]}")

#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується
    def exchenge(self, amount,from_currency, to_currency):
        # self.is_currency(to_currency)
        # self.is_currency(from_currency)

        exchange_amount = amount * self.exchange_rates[from_currency]/self.exchange_rates[to_currency]
        print(f"{amount} {self.currency_ukr[from_currency] } по курсу"
              f"  = {exchange_amount} {self.currency_ukr[to_currency]} ")


    #  зміна валюти
    #  поповнення балансу(валюта та сама)
    #  зняття грошей з балансу(валюта та сама).
    def change_currency(self, currency):
        self.is_currency(currency)
        if currency != self.currency:
            self.balans = self.


client = Bank("Jhon", 2000, "usd")
client.print_info()
client.exchenge(500, 'usd', 'grn')
