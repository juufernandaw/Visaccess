import sqlite3


class PaisDAO:
    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pais (
                nome TEXT PRIMARY KEY NOT NULL,
                isento BOOLEAN NOT NULL
            )
        """)
        self.conn.commit()

    def cadastrar_pais(self, nome, isento):
        self.cursor.execute(
            "INSERT INTO pais (nome, isento) VALUES (?, ?)",
            (nome, isento)
        )
        self.conn.commit()

    def buscar_pais_por_nome(self, nome):
        self.cursor.execute("SELECT * FROM pais WHERE nome=?", (nome,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'nome': row[0], 'isento': row[1]}

    def buscar_todos_paises(self):
        self.cursor.execute("SELECT * FROM pais")
        rows = self.cursor.fetchall()
        paises = []
        for row in rows:
            pais = {'nome': row[0], 'isento': row[1]}
            paises.append(pais)
        return paises
    
    def listar_todos_paises_cadastrados(self):
        self.cursor.execute("SELECT * FROM pais")
        rows = self.cursor.fetchall()
        paises = []
        for row in rows:
            pais = row[0]
            paises.append(pais)
        return paises

    def atualizar_pais(self, nome_novo, isento, nome_antigo):
        self.cursor.execute(
            "UPDATE pais SET nome=?, isento=? WHERE nome=?",
            (nome_novo, isento, nome_antigo)
        )
        self.conn.commit()

    def excluir_pais(self, nome):
        self.cursor.execute("DELETE FROM pais WHERE nome=?", (nome,))
        self.conn.commit()
