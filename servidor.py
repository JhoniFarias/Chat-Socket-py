from socket import *
import threading

HOST = ''
PORT = 5000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

listaClient = set()


def envia_cliente(client_conn):
    while True:

        data = client_conn.recv(1024)

        if(not data):
            print(client_conn.getpeername(), 'saiu')
            return

        dataConvert = str(data, 'utf-8')
        dataView = dataConvert.replace(',','')

        print(dataView)

        for c in listaClient:
            c.send(data)


print("AGUARDANDO CONEXÃO")
while True:
    conn, addr = s.accept()
    print('Cliente Conectado', addr)
    listaClient.add(conn)
    threading.Thread(target=envia_cliente, args=(conn,)).start()


while True:
    data = conn.recv(1024)
    print("Recebido -  ", repr(data))
    conn.sendall(data)
conn.close()
input()
