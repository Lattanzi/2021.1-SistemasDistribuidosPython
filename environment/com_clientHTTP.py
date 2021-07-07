from socket import *

s = socket()

servidor = "g1.globo.com"
porta = 88

s.connect((servidor,porta))

minhareq = "GET /tecnologia/blog/segurança-digital/post/chrome-marcara-sites-sem-criptografia-como-nao-seguros.html HTTP/1.1\r\nHost: g1.globo.com\r\n\r\n"
#print(minhareq)
meusbytes = str.encode(minhareq, "UTF-8")
#print(meusbytes)
s.send(meusbytes)

bytes=''
while True:
    data = s.recv(8192)
    if len(data) == 0:
        break
    print(data.decode())
    
s.close()

#print(bytes)
#print(bytes.decode("UTF-8"))