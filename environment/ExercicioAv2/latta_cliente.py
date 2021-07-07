import requests
import urllib.parse
import json

api = "http://127.0.0.1:8080/anos"
url = api

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))

anoM=0
valorM=0

for ano in dados:
    total=0
    api2 = "http://127.0.0.1:8080/vendas_por_ano/"
    url = f"{api2}{ano['Ano']}"
    dados2 = requests.get(url).json()
    
    for venda in dados2:
        api3 = "http://127.0.0.1:8080/valor_por_venda/"
        url = f"{api3}{venda['InvoiceId']}"
        valor = requests.get(url).json()
        total += valor[0]["Total"]
        
    if total > valorM:
        valorM = total
        anoM = ano["Ano"]
        
print(f"O ano de maior volume de vendas na Chinook foi {anoM} com {valorM:.2f}")

