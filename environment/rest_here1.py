import requests
import urllib.parse
import json

api = "https://geocode.search.hereapi.com/v1/geocode?"
#q=Gast%C3%A3o+Gon%C3%A7alvez%2C+79&apiKey=atwrA9c1lDtmfkUgldwpeaXR7Ycty6Xzh4OYR1lLuhw&lang=pt-BR
#Gastão Gonçalvez, 79

apiKey = "atwrA9c1lDtmfkUgldwpeaXR7Ycty6Xzh4OYR1lLuhw"
lang = "pt-BR"
endereco = input("Qual o endereco? ")
parametros = urllib.parse.urlencode({'apiKey':apiKey, 'lang':lang, 'q':endereco})
print(parametros)


url = f"{api}{parametros}"
print(url)

dados = requests.get(url).json()
#print (json.dumps(dados, indent=4))

latitude = dados["items"][0]["position"]["lat"]
longitude = dados["items"][0]["position"]["lng"]
print(f"A latitude do endereco é {latitude} e a longitude é {longitude}")