from threading import Thread

def Hello (tid):
    for i in range(5):
        print ("Sou a thread %d - %d"%(tid,i))
    print("Thread %d morrendo..."%(tid))

threads=[]
for i in range (5):
    print ("Criando thread %d"%(i))
    threads.append(Thread (target=Hello, args=(i,)))
    threads[-1].start()

print ("Thread Mae esperando pelas filhas...")

for i in range (5):
    print ("Esperando pela thread %d"%(i))
    threads[i].join()

print ("Thread Mae morrendo...")

