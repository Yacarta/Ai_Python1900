# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency

# # Методи:
# #  pay(amount) – виводить повідомлення
# # o CreditCardPayment – оплата карткою {amount}{currency}
# # o PayPalPayment – оплата PayPal {amount}{currency}
# # o CryptoPayment – оплата криптогаманцем {amount}{currency}
#
# # Напишіть функцію create_payment() яка запитує у  користувача тип рахунку та потрібні атрибути і повертає # об’єкт.
# # Створіть декілька рахунків, добавте їх у список та для  кожної викличте відповідні методи.
#
#
class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата CreditCard {amount} {self.currency} ")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount} {self.currency} ")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата Crypto {amount} {self.currency} ")

# Напишіть функцію create_payment() яка запитує у  користувача тип рахунку та потрібні атрибути і повертає # об’єкт.
# Створіть декілька рахунків, добавте їх у список та для  кожної викличте відповідні методи.
def create_payment():
    print("Типи оплати: CreditCard, PayPal, Crypto")
    type_account = input("Введіть тип оплати: ")
    currency = input("Введіть тип валюти: ")

    if type_account == "CreditCard":
        return CreditCardPayment(currency)
    elif type_account == "PayPal":
        return PayPalPayment(currency)
    elif type_account == "Crypto":
        return CryptoPayment(currency)
    else:
        print("Неправильний тип оплати!")
        return None



payments = []
for i in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)


for payment in payments:
    amount = float(input(f"Введіть сумму: "))
    # amount = float(input(f"Введіть сумму для оплати з {payment}: "))
    payment.pay(amount)


client = create_payment()