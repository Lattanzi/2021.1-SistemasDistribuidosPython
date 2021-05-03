# - gerar um vetor de operações com 100 valores randômicos entre -500 e 500
# - Saldo inicial 1000
# - 3 caixas (um em cada thread)
#   - pegar o valor da operação (valorop) do vetor de operações;
#   - pegar o saldo atual e colocar em outra variável;
#   - atualizar essa variável de acordo com o valorop;
#   - ficar em sleep por um tempo aleatório entre 0 e 2s;
#   - atualizar o saldo;
# - Imprimir o saldo final

# x = vet.pop()

# from threading import Thread
import threading
import time
import random

def atualiza_saldo():
    global vet, saldo, mutex
    
    while True:
        with mutex:
            if len(vet) == 0:
                break
            valorop = vet.pop()
            saldotemp = saldo
            saldotemp += valorop
            time.sleep(random.randint(0,2))
            saldo = saldotemp
            print ("Saldo = %.2f, tam = %d"%(saldo,len(vet)))

vet=[]
for i in range(100):
    vet.append(random.randint(-500,500))
#    vet.append(i)

saldo = 1000

threads=[]
mutex = threading.Lock()

for i in range (3):
    print ("Criando thread %d"%(i))
    threads.append(threading.Thread (target=atualiza_saldo))
    threads[-1].start()
    
for i in range (3):
    print ("Esperando pela thread %d"%(i))
    threads[i].join()
    
print ("Saldo final = %.2f"%(saldo))