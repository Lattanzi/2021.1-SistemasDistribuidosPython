import requests
import urllib.parse
import json

api = "http://127.0.0.1:8080/lista-paises"
url = api

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))
lista = []
num = 0
for i in dados:
    num += 1
    lista = num, [i]
    print(lista)
    
clinum = int(input('Entre com o número referente ao país de escolha: '))
#print(clinum)
clinomep = []
i = 0 
for p in dados:
      
    api2 = "http://127.0.0.1:8080/vendas-por-pais/"
    url2 = f"{api2}{p['Country']}"
    dados2 = requests.get(url).json()
    #print (json.dumps(dados2, indent=4))
    
paises = []  
for t in dados2:
    clinomep = dados2[i]['Country']
    paises += [clinomep]
    #print(clinomep)  
    i += 1
    

print('\n País escolhindo: ',paises[clinum-1])
    #print(dados2)
pais = paises[clinum-1]
lista2 = []
api3 = "http://127.0.0.1:8080/vendas-por-pais/"
url3 = api3 + "'" + pais + "'"
dados3 = requests.get(url3).json()
#print (json.dumps(dados3, indent=4))

cont = 0
tot = []
for j in dados3:
    
    api4 = "http://127.0.0.1:8080/trilhas-da-venda/"
    url4 = f"{api4}{j['InvoiceId']}"
    dados4 = requests.get(url4).json()
    
    #lista2 += dados4[cont]["Name"]
    
    #print (json.dumps(dados4, indent=4))
    
    cont += 1
#print(cont)

n = 0 
nome = []  
for l in dados4:
    name = dados4[n]['Name']
    nome += [name]
    #print(name)  
    n += 1


