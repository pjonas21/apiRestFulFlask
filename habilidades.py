from flask import request, json
from flask_restful import Resource

lista_habilidades = ["Python", "Java", "Flask", "Django"]

class Habilidades(Resource):

    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
            return dados
        else:
            return {"status": "error", "message": "Hability already exisits"}

class ListaHabilidades(Resource):

    def get(self, id):
        return lista_habilidades[id]

    def put(self, id):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades[id] = dados
            return {"status": "success", "message": "Hability updated"}
        else:
            return {"status": "error", "message": "Hability already exisits"}


    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status": "success", "message": "Hability deleted"}