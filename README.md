# API Livros

API em Python (Flask + MySQL) no padrão **MVC**, com os 5 endpoints de um CRUD e documentação no **Swagger**.

## Estrutura

```
api-livros/
├── config/
│   └── conexao.py           -> abre a conexão com o MySQL
├── model/
│   └── Livro.py             -> classe Livro: faz o SQL no banco
├── view/
│   └── LivroView.py         -> monta as respostas em JSON
├── controller/
│   └── LivroController.py   -> recebe a requisição, chama o Model e responde pela View
├── app.py                   -> cria a API, define as rotas e liga o Swagger
├── banco.sql                -> script que cria o banco e a tabela Livros
└── requirements.txt         -> bibliotecas do projeto
```

- Tabela no plural: **Livros** (7 colunas: id, titulo, autor, genero, ano_publicacao, paginas, editora)
- Model no singular: arquivo **Livro.py** e classe **Livro**

## Endpoints

| Ação              | Método | Rota            |
|-------------------|--------|-----------------|
| Consultar tudo    | GET    | `/livros`       |
| Consultar por ID  | GET    | `/livros/<id>`  |
| Cadastrar         | POST   | `/livros`       |
| Atualizar         | PUT    | `/livros/<id>`  |
| Excluir           | DELETE | `/livros/<id>`  |

Exemplo de JSON para cadastrar ou atualizar:

```json
{
  "titulo": "A Hora da Estrela",
  "autor": "Clarice Lispector",
  "genero": "Romance",
  "ano_publicacao": 1977,
  "paginas": 88,
  "editora": "Rocco"
}
```

## Como rodar

1. Crie o banco: abra o `banco.sql` no MySQL Workbench (ou phpMyAdmin) e execute.
2. Se o seu MySQL tiver senha, coloque-a em `config/conexao.py`.
3. No terminal, dentro da pasta do projeto:

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

4. Acesse:
   - http://localhost:5000/livros → lista de livros em JSON
   - http://localhost:5000/apidocs → Swagger (dá para testar todos os endpoints por lá)

## Caminho de uma requisição

Exemplo: `GET /livros/1`

1. O **app.py** recebe a rota `/livros/1` e chama `LivroController.buscar_por_id(1)`.
2. O **Controller** pede o livro ao Model: `Livro.buscar_por_id(1)`.
3. O **Model** abre a conexão (pelo `config/conexao.py`), executa `SELECT * FROM Livros WHERE id = 1` e devolve o resultado.
4. O **Controller** confere o resultado: se não existir, devolve erro 404; se existir, manda para a View.
5. A **View** transforma em JSON e devolve com o status 200.

Resumo do MVC:
- **Model** = acessa o banco (SQL)
- **View** = formata a resposta (JSON)
- **Controller** = faz a ponte entre os dois e decide o que responder
- **Config** = dados da conexão com o banco
