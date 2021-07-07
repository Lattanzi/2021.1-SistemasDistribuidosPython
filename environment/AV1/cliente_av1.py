from socket import *

s = socket()

servidor = "127.0.0.1"
porta = 8792

s.connect((servidor, porta))


meuuser = input("Usuário:")
meusbytes = str.encode(meuuser, "UTF-8")

s.send(meusbytes)

# resposta=''
while True:
    paciente = input("I:")
    meusbytes = str.encode(paciente, "UTF-8")
    
    s.send(meusbytes)
    data = s.recv(8192)
    
    resposta = data.decode()
    
    print(resposta)
    
s.close()

