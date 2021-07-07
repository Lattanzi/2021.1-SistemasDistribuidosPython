from flask import Flask
from flask_jsonpify import jsonify
from myconn import conecta_chinook

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

@app.route("/cliente_da_venda/<id>")
def get_cliente_da_venda(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select CustomerId from invoices WHERE InvoiceId={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/nome_do_cliente/<id>")
def get_nome_do_cliente(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select FirstName, LastName from customers WHERE (CustomerId)={id}")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)


app.run (port=8080,debug=True)