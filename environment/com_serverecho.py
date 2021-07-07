from socket import *
from threading import *
import time

def trata_conn (conn, cliente):
    data = conn.recv(8192)
    
    time.sleep(10)
    
    resp = data.decode()
    print("%s me mandou %s"%(str(cliente),resp))
    
    conn.send(str.encode("Eu sei que voce me mandou "+resp))
    
    conn.close()

s = socket()

s.bind(("0.0.0.0", 8752))
s.listen()

print("Servidor no ar...")

while True:
    (conn,cliente) = s.accept()
    print("%s se conectou"%(str(cliente)))
    
    t = Thread (target=trata_conn, args=(conn,cliente))
    t.start()