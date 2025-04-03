import socket
import json
import threading
# Сервер
#  send_message(from_client, to_client)
# o from_client – клієнт від якого отримуємо
# повідомлення
# o to_client – клієнт якому надсилаємо повідомлення
# У функції має використовуватись цикл while
# Основна програма:
#  створити сервер
#  підключити двох клієнтів
#  створити 2 потоки з функцією send_message
#  запустити поток



def send_message(from_client, to_client):
    while True:
        message = from_client.recv(1024).decode()
        if not message:
            break
        to_client.send(message.encode())
        data1 = json.loads(message)
        if data1['message'] == '' :
            break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))

server.listen(2)

from_client, addr1 = server.accept()

to_client, addr2 = server.accept()


thread1 = threading.Thread(target=send_message, args=(from_client, to_client))
thread2 = threading.Thread(target=send_message, args=(to_client, from_client))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

from_client.close()
to_client.close()

server.close()


#_____________________________CLIENT 1 TA 2

# Додайте до попереднього завдання потоки, щоб клієнти
# могли спілкуватись не обов’язково по черзі. Для цього
# Практичне завдання
# напишіть функції
# Клієнт:
#  receive_message(client) – отримує повідомлення від сервера
# та виводить на екран. Має використовуватись цикл while
# Основна програма:
#  підключитись до сервера
#  створити потік з функцією receive_message
#  запустити потік
#  попросити користувача ввести ім’я
#  створити цикл в якому користувач вводить повідомлення та
# надсилає на сервер



import socket
import json
import threading

def receive_message(client):
    while True:
        receive = client.recv(1024).decode()
        data = json.loads(receive)
        print(f"{data['name']} відправив(ла) {data['message']}")

        if data['message'] == '':
            break



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

thread = threading.Thread(target=receive_message, args=(client,))
thread.start()

print("Чат")
name = input('Як вас звати? >>> ')

while True:
    message = input()

    data = {'name': name,
            'message': message}
    code = json.dumps(data)
    client.send(code.encode())

    if message =='':
        break

thread.join()
client.close()
