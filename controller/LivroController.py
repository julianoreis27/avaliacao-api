from flask import request
from model.Livro import Livro
from view.LivroView import LivroView


# CONTROLLER: recebe a requisição, chama o Model e devolve a resposta pela View
class LivroController:

    @staticmethod
    def listar_todos():
        livros = Livro.listar_todos()
        return LivroView.sucesso(livros)

    @staticmethod
    def buscar_por_id(id):
        livro = Livro.buscar_por_id(id)
        if livro is None:
            return LivroView.erro("Livro não encontrado", 404)
        return LivroView.sucesso(livro)

    @staticmethod
    def cadastrar():
        dados = request.get_json()  # pega o JSON enviado no corpo da requisição
        if not dados or not dados.get("titulo") or not dados.get("autor"):
            return LivroView.erro("Os campos 'titulo' e 'autor' são obrigatórios", 400)
        novo_id = Livro.cadastrar(dados)
        return LivroView.sucesso({"mensagem": "Livro cadastrado com sucesso", "id": novo_id}, 201)

    @staticmethod
    def atualizar(id):
        if Livro.buscar_por_id(id) is None:
            return LivroView.erro("Livro não encontrado", 404)
        dados = request.get_json()
        if not dados or not dados.get("titulo") or not dados.get("autor"):
            return LivroView.erro("Os campos 'titulo' e 'autor' são obrigatórios", 400)
        Livro.atualizar(id, dados)
        return LivroView.mensagem("Livro atualizado com sucesso")

    @staticmethod
    def excluir(id):
        if Livro.buscar_por_id(id) is None:
            return LivroView.erro("Livro não encontrado", 404)
        Livro.excluir(id)
        return LivroView.mensagem("Livro excluído com sucesso")
