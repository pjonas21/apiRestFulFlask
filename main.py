from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades
import json

app = Flask(__name__)
api = Api(app)

lista_devs = [
    {"nome": "Paulo",
     "habilidadedes": [
         "Python", "Java", "Django"
     ]
     },
    {"nome": "Jonas",
     "habilidadedes": [
         "Python", "JavaScript", "Angular"
     ]
     }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = lista_devs[id]
        except IndexError:
            response = {"status": "erro", "mensagem": "Desenvolvedor nao existe"}
        except Exception:
            response = {"status": "erro", "mensagem": "Procure o administrador da API"}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_devs[id] = dados
        return dados

    def delete(self, id):
        lista_devs.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluido."}


class ListaDesenvolvedores(Resource):
    def get(self):
        return {"lista_devs": lista_devs}

    def post(self):
        dados = json.loads(request.data)
        lista_devs.append(dados)
        return {"status": "sucesso", "mensagem": "Desevolvedor inserido com sucesso"}



api.add_resource(Desenvolvedor, "/dev/<int:id>")
api.add_resource(ListaDesenvolvedores, "/lista_devs")
api.add_resource(Habilidades, "/habilidades")
api.add_resource(ListaHabilidades, "/lista_habilidades/<int:id>")

if __name__ == '__main__':
    app.run()
