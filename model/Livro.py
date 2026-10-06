from config.conexao import conectar


# MODEL: única parte que conversa com o banco de dados (faz o SQL)
class Livro:

    @staticmethod
    def listar_todos():
        conexao = conectar()
        # dictionary=True devolve cada linha como {coluna: valor}
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Livros")
        livros = cursor.fetchall()
        cursor.close()
        conexao.close()
        return livros

    @staticmethod
    def buscar_por_id(id):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Livros WHERE id = %s", (id,))
        livro = cursor.fetchone()  # devolve None se não encontrar
        cursor.close()
        conexao.close()
        return livro

    @staticmethod
    def cadastrar(dados):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO Livros
                 (titulo, autor, genero, ano_publicacao, paginas, editora)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (dados.get("titulo"), dados.get("autor"), dados.get("genero"),
                   dados.get("ano_publicacao"), dados.get("paginas"),
                   dados.get("editora"))
        cursor.execute(sql, valores)
        conexao.commit()  # confirma a gravação no banco
        novo_id = cursor.lastrowid  # id gerado pelo AUTO_INCREMENT
        cursor.close()
        conexao.close()
        return novo_id

    @staticmethod
    def atualizar(id, dados):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Livros
                 SET titulo = %s, autor = %s, genero = %s,
                     ano_publicacao = %s, paginas = %s, editora = %s
                 WHERE id = %s"""
        valores = (dados.get("titulo"), dados.get("autor"), dados.get("genero"),
                   dados.get("ano_publicacao"), dados.get("paginas"),
                   dados.get("editora"), id)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def excluir(id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Livros WHERE id = %s", (id,))
        conexao.commit()
        cursor.close()
        conexao.close()
