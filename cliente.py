import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
from tkinter import *

frame_ip = Tk()
frame_ip.title("Digite o endereco IP para se Conectar")

def altera_janela():
    frame_ip.quit()
    


host = Entry(frame_ip)
host.pack()

btnEnviar = Button(frame_ip, text="Conectar", command=altera_janela)
btnEnviar.pack()
frame_ip.geometry("200x200")
frame_ip.mainloop()


PORT = 5000
ADDR = (host.get(), PORT)

client_socket = socket.socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect(ADDR)


def recebe_mensagem():
    while True:
        try:
            msg = client_socket.recv(2048).decode("utf8")
            listaMensagem.insert(END, msg)
        except OSError:  
            break


def enviar_mensagem(event=None):
    msg = inputMensagem.get()
    inputMensagem.delete(0, END)
    client_socket.send(bytes(msg, "utf8"))


janela = Tk()
janela.title("Comunicação Criptografada")


container_mensagem = Frame(janela)


listaMensagem = Listbox(container_mensagem, height=15, width=50)
listaMensagem.pack(side=LEFT, fill=BOTH)
listaMensagem.pack()
container_mensagem.pack()

inputMensagem = Entry(janela)

inputMensagem.bind("<Return>", enviar_mensagem)
inputMensagem.pack()
btnEnviar = Button(janela, text="Enviar", command=enviar_mensagem)
btnEnviar.pack()

recebe_mensagemThread = Thread(target=recebe_mensagem)
recebe_mensagemThread.start()


janela.mainloop()
