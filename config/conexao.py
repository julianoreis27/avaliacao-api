import mysql.connector


# Abre e devolve uma conexão com o banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # coloque aqui a senha do seu MySQL (no XAMPP é vazia)
        database="biblioteca"
    )
