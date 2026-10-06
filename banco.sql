-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- Tabela no PLURAL, com 7 colunas
CREATE TABLE IF NOT EXISTS Livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    ano_publicacao INT,
    paginas INT,
    editora VARCHAR(100)
);

-- Alguns registros para testar
INSERT INTO Livros (titulo, autor, genero, ano_publicacao, paginas, editora) VALUES
('Dom Casmurro', 'Machado de Assis', 'Romance', 1899, 256, 'Garnier'),
('O Hobbit', 'J. R. R. Tolkien', 'Fantasia', 1937, 310, 'HarperCollins'),
('1984', 'George Orwell', 'Ficção', 1949, 328, 'Companhia das Letras'),
('Capitães da Areia', 'Jorge Amado', 'Romance', 1937, 280, 'Companhia das Letras');
