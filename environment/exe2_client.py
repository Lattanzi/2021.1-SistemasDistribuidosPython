from socket import *

s = socket()

servidor = "127.0.0.1"
porta = 8729

s.connect((servidor, porta))
# s.settimeout(12)

meuuser = input("Digite seu usuário: ")
meusbytes = str.encode(meuuser, "UTF-8")
# print(meusbytes)
s.send(meusbytes)

# resposta=''
while True:
    minhastr = input("Entre com seu CPF: ")
    meusbytes = str.encode(minhastr, "UTF-8")
    # print(meusbytes)
    s.send(meusbytes)
    data = s.recv(8192)
    # if len(data) == 0:
    #     break
    resposta = data.decode()
    
    print(resposta)
    
s.close()

# print("O servidor enviou: %s"%(resposta))