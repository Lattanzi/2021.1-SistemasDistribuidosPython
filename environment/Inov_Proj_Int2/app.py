from pacienteController import PacienteController


from flask import Flask
app = Flask(__name__)

@app.route('/index')
def responde():
    pacienteInstancia = PacienteController()
    lista = pacienteInstancia.retornaJson()
    return str(lista)

app.run()
