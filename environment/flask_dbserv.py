from flask import Flask
from myconn import conecta_chinook
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route("/")
def imprime():
    return "SD é fácil"
    
@app.route("/clientes")
def get_clientes():
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute ("select CustomerId,FirstName,LastName from customers")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    return jsonify(lista)

@app.route("/cliente/<id>")
def get_cliente_por_id(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select CustomerId,FirstName,LastName,Address,City,State,Country from customers where CustomerId={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    return jsonify(lista)

@app.route("/nome/<nome>")
def imprime_nome(nome):
    return f"Seu nome é {nome}"


app.run (port=8080,debug=True)