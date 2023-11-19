from flask import request, json
from flask_restful import Resource

lista_habilidades = ["Python", "Java", "Flask", "Django"]

class Habilidades(Resource):

    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return dados

class ListaHabilidades(Resource):

    def get(self, id):
        return lista_habilidades[id]

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return {"status": "success", "message": "Hability updated"}

    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status": "success", "message": "Hability deleted"}