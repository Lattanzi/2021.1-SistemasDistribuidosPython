from flask import Flask
from flask_jsonpify import jsonify
import mysql.connector

def conecta_chinook():
    conn = mysql.connector.connect (host=" ", port=" "
    , user=" ", passwd=" ", database="chinook")
    
    cursor = conn.cursor()
    
    return conn

app = Flask(__name__)
    
@app.route("/paises")
def get_paises():
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute ("select BillingCountry from invoices WHERE ")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/id_cliente/<pais>")
def get_id_cliente(pais):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select CustomerId from invoices WHERE BillingCountry='{pais}'")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/cliente_endereco/<id>")
def get_cliente_endereco(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select Address, City, State from customers WHERE CustomerId={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/nome_do_cliente/<id>")
def get_nome_do_cliente(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    #cursor.execute (f"select c.FirstName, c.LastName from customers c, invoices i where (c.CustomerId)='{id}'and c.CustomerId = i.CustomerId")
    cursor.execute (f"select FirstName, LastName from customers WHERE CustomerId={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)


app.run (port=8080,debug=True)
