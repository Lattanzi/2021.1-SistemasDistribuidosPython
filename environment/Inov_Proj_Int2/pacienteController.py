from paciente import Paciente
import json
class PacienteController:

   
    listaPaciente = []
    listaJson = []

    def __init__(self):
        self.preencheListaPaciente()

    
    def preencheListaPaciente(self):
        print("entrou ")
        
        paciente = []

        for i in range (10):
            paciente.append(Paciente())
            paciente[i].nome = "Joao"+str(i)
            paciente[i].telefone = "981855228"
            paciente[i].endereco = "rua"+str(i)
            paciente[i].email =paciente[i].nome+"@gmail.com"
            self.listaPaciente.append(paciente[i])
            print(paciente[i].nome)
        
        for i in range (10):
            self.listaJson.append(json.dumps(self.listaPaciente[i].__dict__))

    def retornaJson(self):
        return self.listaJson    