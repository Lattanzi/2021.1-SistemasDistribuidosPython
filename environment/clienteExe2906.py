import requests
import urllib.parse
import json

#serverapi = "http://127.0.0.1:8080/anos"
#serverurl = serverapi

#dados = requests.get(serverurl).json()
#print (json.dumps(dados, indent=4))

api = "https://geocode.search.hereapi.com/v1/geocode?"

apiKey="CBQbQVDYb0qt0_eIHFr_p8fefJ40YzVgsBB02vjO6VQ"
lang="pt-BR"

endereco = input ("Qual o primeiro endereço? ")

parametros = urllib.parse.urlencode({'apiKey':apiKey, 'lang':lang, 'q':endereco})
#print (parametros)
url=f"{api}{parametros}"
print (url)

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))

latitude1 = dados["items"][0]["position"]["lat"]
longitude1 = dados["items"][0]["position"]["lng"]

print (f"A latitude do primeiro endereço é {latitude1} e a longitude é {longitude1}")

endereco = input ("Qual o segundo endereço? ")

parametros = urllib.parse.urlencode({'apiKey':apiKey, 'lang':lang, 'q':endereco})
#print (parametros)
url=f"{api}{parametros}"
print (url)

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))

latitude2 = dados["items"][0]["position"]["lat"]
longitude2 = dados["items"][0]["position"]["lng"]

print (f"A latitude do segundo endereço é {latitude2} e a longitude é {longitude2}")

#https://router.hereapi.com/v8/routes?transportMode=car&origin=52.5308,13.3847&destination=52.5264,13.3686&return=summary&apiKey=CBQbQVDYb0qt0_eIHFr_p8fefJ40YzVgsBB02vjO6VQ
api2 = "https://router.hereapi.com/v8/routes?"
parametros = urllib.parse.urlencode({'apiKey':apiKey, 'return':'summary', 'lang':lang, 'transportMode':'car', 'origin':f"{latitude1},{longitude1}", 'destination':f"{latitude2},{longitude2}"})
url=f"{api2}{parametros}"
print (url)

dados = requests.get(url).json()
print (json.dumps(dados, indent=4))

print (f"A distância entre os dois endereços é:{dados['routes'][0]['sections'][0]['summary']['length']} metros")
