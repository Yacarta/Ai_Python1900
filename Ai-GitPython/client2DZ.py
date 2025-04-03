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
    client.close()



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

thread = threading.Thread(target=receive_message, args=(client,))
thread.start()

print("Ви в чаті")
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