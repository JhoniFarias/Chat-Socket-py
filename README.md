
# Chat Socket Python
projeto de faculdade para conclusão de semestre, foi proposto o desenvolvimento de um sistema com comunicação via rede,
utilizando sockets, e todas as mensagemm criptografadas, para trafegar via rede.

# Projeto em python, utilizando as seguintes tecnologias:

<h2>Tkinter</h2>
usado para montar toda a parte de interface.

<h2>Sockets</h2>
para comunicação via rede, todos os teste foram realizado localhost, com todas as maquinas conectadas na mesma rede.

<h2>Criptografia</h2>
o algoritmo de criptografia utilizado foi a <b>Cifra de César</b> proposto pelo professor, é um algoritmo muito simples, foi usado apenas para entender o conceito de criptografia

# Como funciona ? 
Funciona de forma client X Server -> o Server fica responsável por abrir o canal de comunicação e direcionar todas as mensagems a todos os clientes conectados.
o algoritmo de criptografia fica no client, ou seja, todas as mensagem chegam criptografadas no servidor.

<h2>Server.py</h2>

Primeiro devemos o "startar" o arquivo <b>servidor.py</b>. esse arquivo que gerencia o canal de comunição via socket.

Obs: ao iniciar o server.py exibe um mensagem no console AGUARDANDO CONEXÃO, quando o client consegue se conectar ao server, automaticamente é feito o log com IP e a porta utilizada

<img src="https://github.com/JhoniFarias/Chat-Socket-python/blob/master/prints/Servidor%20-%20Recebendo%20Conex%C3%A3o.PNG"/>


<h2>client.py</h2>

Ao startar o client.py aparece a seguinte tela, onde devemos digitar o nome de usuario e IP local (IPV4)

<img src="https://github.com/JhoniFarias/Chat-Socket-python/blob/master/prints/Login.PNG" />

Tela do chat logo após realizar o login

<img src="https://github.com/JhoniFarias/Chat-Socket-python/blob/master/prints/Chat%20-%20Mensagem%20Descriptografada.PNG"/>

exemplo de como a mensagem é recebida no server.

<img src="https://github.com/JhoniFarias/Chat-Socket-python/blob/master/prints/Mensagem%20Criptografada.PNG">




