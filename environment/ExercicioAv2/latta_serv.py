from flask import Flask
from flask_jsonpify import jsonify
import mysql.connector

def conecta_chinook():
    conn = mysql.connector.connect (host=" ", port=" "
    , user=" ", passwd=" ", database="chinook")
    
    cursor = conn.cursor()
    
    return conn

app = Flask(__name__)
    
@app.route("/anos")
def get_clientes():
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute ("select DISTINCT YEAR(InvoiceDate) as Ano from invoices")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/vendas_por_ano/<ano>")
def get_vendas_por_ano(ano):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select InvoiceId from invoices WHERE YEAR(InvoiceDate)='{ano}'")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/valor_por_venda/<id>")
def get_valor_por_venda(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select Total from invoices WHERE InvoiceId={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)


app.run (port=8080,debug=True)
