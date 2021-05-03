from socket import *
import threading

def tem_msg ():
	return len(mensagens) > 0

def envia ():
	global mensagens, alunos
	while True:
		print (mensagens)
		with cv:
			cv.wait ()

		print ("Enviando Mensagens...")

		with mutex:
			for m in mensagens:
				print ("Enviando "+m[1].decode("utf-8")+"...")
				for c in conexoes:
					if not (c is None):
						if m[0][0] in alunos:
							al = alunos[m[0][0]]
						else:
							al = m[0]
						minhastr = "[" + str(al) + "]: " + m[1].decode("utf-8")
						c[0].send (str.encode(minhastr, "utf-8"))
			mensagens = []
			
def atende (conn, cliente, ident):
	global conexoes
	data = conn.recv (4096)
	alunos[cliente[0]] = data.decode()
	while True:
		try:
			data = conn.recv (4096)
		except Exception:
			break;

		if not data or len(data) == 0:
			break

		print (str(cliente)+" me mandou "+data.decode("utf-8") )

		with mutex:
			mensagens.append ((cliente, data))

		with cv:
			cv.notify ()

#                conn.send (str.encode ("Eu sei que voce me mandou "+data.decode("utf-8") , "UTF-8"))

	print ("Fim da conexao com "+str(cliente))

	conn.close ()
	with mutex2:
		conexoes[ident-1] = None


s = socket ()

host = "0.0.0.0"
porta = 8752
s.bind ((host, porta))
s.listen (10)
nthr = 0
alunos = {}

mutex = threading.Lock ()
mutex2 = threading.Lock ()
cv = threading.Condition()
mensagens = []
conexoes = []

print ("Criando thread de envio")
t = threading.Thread(target=envia,args=())
t.start()

while True:
	(conn, cliente) = s.accept ()
	with mutex2:
		conexoes.append ([conn, cliente])

	print ("Recebi a conexao de "+str(cliente))
	nthr += 1
	print ("Criando thread "+str(nthr))
	t = threading.Thread(target=atende,args=(conn, cliente, nthr, ))
	t.start()