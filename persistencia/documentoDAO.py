import sqlite3
from entidades.documento import Documento


class DocumentoDAO:
    def __init__(self):
        self.banco = sqlite3.connect('visaccess.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS documento (
                nome TEXT NOT NULL,
                regra TEXT NOT NULL,
                PRIMARY KEY(nome)
        );
        """)

    def close(self):
        self.banco.close()

    def get_all_documentos(self):
        print('Entrou no get_all_documentos DAO')
        self.cursor.execute("SELECT * FROM documento")
        rows = self.cursor.fetchall()
        documentos = []
        for row in rows:
            documento = {'nome': row[0], 'regra': row[1]}
            documentos.append(documento)
        return documentos

    def registra_documento(self, nome: str, regra: str):
        self.cursor.execute("INSERT INTO documento (nome, regra) VALUES (?, ?)", [nome, regra])
        self.banco.commit()

    def remove_documento(self, nome: str):
        self.cursor.execute("DELETE FROM documento WHERE nome=?", [nome])
        self.banco.commit()

    def altera_documento(self, novo_nome, nova_regra, velho_nome):
        print('entrou no altera_documento')
        self.cursor.execute(
            f"UPDATE documento SET nome='{novo_nome}', regra='{nova_regra}' WHERE nome=?", [velho_nome])
        self.banco.commit()
