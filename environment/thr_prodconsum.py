import threading
import random
import time

buffer=[]
MAX=10

sincond = threading.Condition ()

def tem_espaco ():
    return len(buffer) < MAX

def func_prod():
    while True:
        with sincond:
            sincond.wait_for(tem_espaco)
            num=random.randint(1, 50)
            buffer.append(num)
            print("Numero %d acrescentado.\n"%(num))
            sincond.notify()
        time.sleep(random.randint(0,1))
    return 0

def tem_dado ():
    return len(buffer) > 0
    
def func_consum():
    while True:
        with sincond:
            sincond.wait_for(tem_dado)
            num=buffer.pop(0)
            print("Numero %d retirado.\n"%(num))
            sincond.notify()
        time.sleep(random.randint(0,1))
    return 0
    
produtor=threading.Thread (target=func_prod)
consumidor=threading.Thread (target=func_consum)

produtor.start()
consumidor.start()

produtor.join()
consumidor.join()


