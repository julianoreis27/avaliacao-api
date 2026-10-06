from flask import Flask
from flasgger import Swagger
from controller.LivroController import LivroController

app = Flask(__name__)
app.json.sort_keys = False  # mantém a ordem das colunas no JSON
app.json.ensure_ascii = False  # mostra acentos normalmente no JSON

# Swagger: documentação e testes em http://localhost:5000/apidocs
Swagger(app, template={"info": {"title": "API Livros", "version": "1.0",
                                "description": "API de cadastro de livros (MVC com Flask e MySQL)"}})


@app.route("/livros", methods=["GET"])
def listar_livros():
    """
    Consultar todos os livros
    ---
    tags: [Livros]
    responses:
      200:
        description: Lista de livros
    """
    return LivroController.listar_todos()


@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    """
    Consultar um livro pelo ID
    ---
    tags: [Livros]
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Livro encontrado
      404:
        description: Livro não encontrado
    """
    return LivroController.buscar_por_id(id)


@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    """
    Cadastrar um novo livro
    ---
    tags: [Livros]
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          example:
            titulo: "A Hora da Estrela"
            autor: "Clarice Lispector"
            genero: "Romance"
            ano_publicacao: 1977
            paginas: 88
            editora: "Rocco"
    responses:
      201:
        description: Livro cadastrado
      400:
        description: Dados inválidos
    """
    return LivroController.cadastrar()


@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    """
    Atualizar um livro
    ---
    tags: [Livros]
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          example:
            titulo: "Dom Casmurro"
            autor: "Machado de Assis"
            genero: "Romance"
            ano_publicacao: 1899
            paginas: 300
            editora: "Penguin"
    responses:
      200:
        description: Livro atualizado
      404:
        description: Livro não encontrado
    """
    return LivroController.atualizar(id)


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    """
    Excluir um livro
    ---
    tags: [Livros]
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Livro excluído
      404:
        description: Livro não encontrado
    """
    return LivroController.excluir(id)


if __name__ == "__main__":
    app.run(debug=True)
