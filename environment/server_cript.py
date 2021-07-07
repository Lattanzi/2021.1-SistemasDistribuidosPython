from socket import *
from threading import *

#função que trata conexão com cliente
def trata_conn(conn,cliente):
    while True:     
        dados=conn.recv(1024)
        mensagem=dados.decode("utf-8")
        if(mensagem == ""):
            break
        else:
            mensagemcriptografada = Criptografa(mensagem)
            conn.send(str.encode(mensagemcriptografada,"UTF-8"))

#função que criptografa a mensagem do cliente
def Criptografa(mensagem):
    
    czenit="ZENITzenit"
    cpolar="POLARpolar"
    
    troca=""
    for x in mensagem:
        if x in cpolar:
            i=cpolar.index(x)
            troca+=czenit[i]
        elif x in czenit:        
            i=czenit.index(x)
            troca+=cpolar[i]
        else:
            troca += x
    return troca


s=socket()
host="0.0.0.0"   
porta=8729
s.bind((host,porta))
s.listen()

while True:                                 
    (conn,cliente)=s.accept()
    
    t=Thread(target=trata_conn,args=(conn,cliente)) 
    t.start()