from flask import jsonify


# VIEW: monta a resposta em JSON que o cliente vai receber
class LivroView:

    @staticmethod
    def sucesso(dados, status=200):
        return jsonify(dados), status

    @staticmethod
    def mensagem(texto, status=200):
        return jsonify({"mensagem": texto}), status

    @staticmethod
    def erro(texto, status=400):
        return jsonify({"erro": texto}), status
