import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
from tkinter import Frame
from tkinter import Listbox
from tkinter import LEFT
from tkinter import BOTH
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import END

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import LOGIN_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TelaPrincipal (root)
    LOGIN_support.init(root, top)
    root.mainloop()

w = None
def create_TelaPrincipal(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TelaPrincipal (w)
    LOGIN_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TelaPrincipal():
    global w
    w.destroy()
    w = None

class TelaPrincipal:
    def chatConnect(self):
        PORT = 5000
        ADDR = (self.IPusuario.get(), PORT)

        client_socket = socket.socket(AF_INET, SOCK_STREAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client_socket.connect(ADDR)


        def recebe_mensagem():
            while True:
                try:
                    msgCrypt = client_socket.recv(2048).decode("utf8")            
                    wordsArray = msgCrypt.split(',')
                    final = ""
                    for n in wordsArray:
                        l = int(n)
                        l = l - 20
                        l = chr(l)
                        final = final + l

                    listaMensagem.insert(END, final)
                except OSError:  
                    break


        def enviar_mensagem(event=None):
            msg = inputMensagem.get()
            inputMensagem.delete(0, END)
            
            v = []

            for letra in msg:
                l = ord(letra) + 20
                v.append(l)

        
            msgCrypt = ','.join(map(str, v))
            
            client_socket.send(bytes(msgCrypt, "utf8"))

        janela = tk.Tk()
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

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 16 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("529x314+404+115")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Login")
        top.configure(background="#1b1b1b")

        self.IPconectar = tk.Label(top)
        self.IPconectar.place(relx=0.189, rely=0.159, height=71, width=354)
        self.IPconectar.configure(background="#1b1b1b")
        self.IPconectar.configure(disabledforeground="#a3a3a3")
        self.IPconectar.configure(font=font9)
        self.IPconectar.configure(foreground="#ffffff")
        self.IPconectar.configure(text='''DIGITE O IP PARA SE CONECTAR:''')

        self.IPusuario = tk.Entry(top)
        self.IPusuario.place(relx=0.227, rely=0.446,height=30, relwidth=0.575)
        self.IPusuario.configure(background="white")
        self.IPusuario.configure(borderwidth="2")
        self.IPusuario.configure(cursor="fleur")
        self.IPusuario.configure(disabledforeground="#a3a3a3")
        self.IPusuario.configure(font="TkFixedFont")
        self.IPusuario.configure(foreground="#000000")
        self.IPusuario.configure(insertbackground="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.BtnConectar = ttk.Button(top)
        self.BtnConectar.place(relx=0.359, rely=0.701, height=35, width=156)
        self.BtnConectar.configure(takefocus="")
        self.BtnConectar.configure(text='''Conectar''')
        self.BtnConectar.configure(cursor="fleur")
        self.BtnConectar.configure(command=self.chatConnect)

if __name__ == '__main__':
    vp_start_gui()




