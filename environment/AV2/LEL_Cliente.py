import requests
import urllib.parse
import json

api = "http://127.0.0.1:8080/anos"
url = api

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))
lista = []

for ano in dados:
    lista1 = []
    total = 0
    api2 = "http://127.0.0.1:8080/vendas_por_ano/"
    url = f"{api2}{ano['Ano']}"
    dados2 = requests.get(url).json()

    for venda in dados2:
        api3 = "http://127.0.0.1:8080/cliente_da_venda/"
        url = f"{api3}{venda['InvoiceId']}"
        valor = requests.get(url).json()
        clienteid = valor[0]["CustomerId"]
        lista1.append(clienteid)

    if ano['Ano'] == dados[0]['Ano']:
        lista = lista1.copy()
    else:
        for id in lista:
            if not id in lista1:
                lista.remove(id)

print('Clientes fiéis: ')
for cli in lista:
    api4 = "http://127.0.0.1:8080/nome_do_cliente/"
    url = f"{api4}{cli}"
    dados3 = requests.get(url).json()
    print(f"\n{dados3[0]['FirstName']} {dados3[0]['LastName']}")