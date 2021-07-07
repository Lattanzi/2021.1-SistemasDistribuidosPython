from flask import Flask
from flask_jsonpify import jsonify
from myconn import conecta_chinook

app = Flask(__name__)
    
@app.route("/lista-paises")
def get_paises():
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute ("select distinct Country from customers where CustomerId in (select CustomerId from invoices where InvoiceId IS NOT NULL) order by Country")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/lista-generos")
def get_generos():
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select GenreId, Name from genres")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/trilhas-da-venda/<id>")
def get_trilhas_da_venda(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select Name from tracks WHERE TrackId in (select TrackId from invoice_items WHERE InvoiceId={id})")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)

@app.route("/genero-da-trilha/<id>")
def get_genero_da_trilha(id):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select Name from genres WHERE GenreId in (select GenreId from tracks WHERE TrackId={id})")
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)
    
@app.route("/vendas-por-pais/<name>")
def get_vendas_por_pais(name):
    conn = conecta_chinook()
    cursor = conn.cursor()
    cursor.execute (f"select InvoiceId from invoices WHERE BillingCountry={name} ") #passar o nome do pais entre '', exemplo: vendas-por-pais/'Germany'
    records = cursor.fetchall()
    lista = [dict(zip(cursor.column_names,x)) for x in records]
    conn.close()
    return jsonify(lista)


app.run (port=8080,debug=True)