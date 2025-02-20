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
# class CreditCardPayment:
#     def __init__(self, currency):
#         self.currency = currency
#
#     @staticmethod
#     def pay( amount):
#         print(f"Оплата CreditCard {amount} {self.currency} ")
#
#
#
# class PayPalPayment:
#     def __init__(self, currency):
#         self.currency = currency
#
#     @staticmethod
#     def pay(amount):
#         print(f"Оплата PayPal {amount} {self.currency} ")
#
#
# class CryptoPayment
#     def __init__(self, currency):
#         self.currency = currency
#
#     @staticmethod
#     def pay(amount):
#         print(f"Оплата Crypto {amount} {self.currency} ")
#
# # Напишіть функцію create_payment() яка запитує у  користувача тип рахунку та потрібні атрибути і повертає # об’єкт.
# # Створіть декілька рахунків, добавте їх у список та для  кожної викличте відповідні методи.
# def create_payment():
#     print("Types of accounts: CreditCard, PayPal, Crypto" )
#     type_acount = input("Enter type of account: ")
#     currency = input("Enter currency")


    if type_acount == "CreditCard" :
        return CreditCardPayment
    elif type_acount == "PayPal":
        return PayPalPayment
    elif type_acount == "Crypto":
        return CryptoPayment

payments =[]
for i in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)

for payment in payments: