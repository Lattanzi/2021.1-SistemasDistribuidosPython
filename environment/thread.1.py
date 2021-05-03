from threading import Thread
import threading
import time
import random

def Hello (tid):
    global soma, mutex
    
    subtotal = 0
    for i in range(5):
        subtotal += i+1
        print ("Sou a thread %d - %d"%(tid,subtotal))
#    mutex.acquire() # DOWN
    with mutex:
        subtotal += soma
        time.sleep(random.randint(0,2))
        soma = subtotal
#    mutex.release() # UP
    print("Thread %d morrendo. Soma = %d"%(tid,subtotal))

soma = 0
threads=[]
mutex = threading.Lock()
for i in range (5):
    print ("Criando thread %d"%(i))
    threads.append(threading.Thread (target=Hello, args=(i,)))
    threads[-1].start()

for i in range (5):
    print ("Esperando pela thread %d"%(i))
    threads[i].join()

print ("Thread Mae morrendo. Soma total = %d"%(soma))

