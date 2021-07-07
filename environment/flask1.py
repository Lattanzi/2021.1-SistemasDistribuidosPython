from flask import Flask

app = Flask(__name__)

@app.route("/")
def imprime():
    return "SD é fácil"

@app.route("/nome/<nome>")
def imprime_nome(nome):
    return f"Seu nome é {nome}"

@app.route("/eca")
def imprime_eca():
    return "Eca"

app.run (port=8080,debug=True)