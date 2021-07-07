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

zenit, polar = 'zenit', 'polar'
final_message = ''
#message = input('message : ')
n = 0
for i in range(len(meuuser)):
    x = meuuser[n]
    if x in zenit:
        x = int(zenit.find(meuuser[n]))
        final_message += polar[x]
    elif x in polar:
        x = int(polar.find(meuuser[n]))
        final_message += zenit[x]
    else:
        final_message += meuuser[n]
    n += 1

print(final_message)

# resposta=''
while True:
    minhastr = input("Digite a mensagem: ")
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