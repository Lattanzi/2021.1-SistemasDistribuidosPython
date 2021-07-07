from socket import *


s=socket()                                                      #instancia socket
s.connect(("localhost",8729))                                   #conecta ao localhost na porta descrita

#le, codifica e envia a mensagem
minhastr=input ("Digite uma mensagem para ser criptografada: ")
meusbytes=str.encode(minhastr,"UTF-8")
s.send(meusbytes)

#recebe a resposta do servidor e decodifica ela
respostaDoServidor = s.recv(1024) 
mensagemCriptografada=respostaDoServidor.decode("utf-8")

#printa a mensagem criptografada
print("A mensagem criptografada é: %s"%(mensagemCriptografada))


#manda a mensagem criptografada para o servidor
meusbytes=str.encode(mensagemCriptografada,"UTF-8")
s.send(meusbytes)

#recebe mensagem descriptografada e decodifica ela
mensagemDescriptografada=s.recv(1024) 
mensagemFinal=mensagemDescriptografada.decode("utf-8")

#compara a mensagem final com a inicial
if(mensagemFinal == minhastr):
    print("a criptografia funcionou")
else:
    print("a criptografia falhou")

#fecha a conexão
s.close()