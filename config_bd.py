import sqlite3

# Conectar-se ao banco de dados ou criá-lo se ele ainda não existe
conn = sqlite3.connect('biblioteca.db')

# Criar a tabela de livros
conn.execute('''CREATE TABLE livros
                (id INT PRIMARY KEY NOT NULL,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INT NOT NULL);''')

# Inserir dados na tabela
conn.execute("INSERT INTO livros (id, titulo, autor, ano_publicacao) \
                VALUES (1, 'Python para Leigos', 'Guido van Rossum', 2020)")

conn.execute("INSERT INTO livros (id, titulo, autor, ano_publicacao) \
                VALUES (2, 'Introdução à Ciência de Dados', 'João da Silva', 2021)")

# Consultar dados da tabela
cursor = conn.execute("SELECT id, titulo, autor, ano_publicacao FROM livros")
for row in cursor:
    print(f"ID = {row[0]}, Título = {row[1]}, Autor = {row[2]}, Ano de Publicação = {row[3]}")

# Fechar a conexão
conn.close()
