import sqlite3
from entidades.solicitacao_de_visto import SolicitacaoDeVisto


class SolicitacaoDeVistoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS solicitacaoDeVisto (id integer PRIMARY KEY AUTOINCREMENT,'
                            'data_solicitacao date NOT NULL,'
                            'estrangeiro TEXT NOT NULL,'
                            'status TEXT NOT NULL,'
                            'visto integer,'
                            'FOREIGN KEY (estrangeiro) REFERENCES estrangeiro, '
                            'FOREIGN KEY (visto) REFERENCES tipos_visto)')

    def close(self):
        self.conn.close()

    def create_solicitacao_visto(self, data_solicitacao, passaporte_estrangeiro, status, nome_visto):
        self.cursor.execute("INSERT INTO solicitacaoDeVisto (data_solicitacao, estrangeiro, status, visto) VALUES (?, ?, ?, ?)",
                            [data_solicitacao, passaporte_estrangeiro, status, nome_visto])
        self.conn.commit()
        id = self.cursor.lastrowid
        print("Instanciando solicitacao de visto")
        obj = SolicitacaoDeVisto(data_solicitacao=data_solicitacao, estrangeiro=passaporte_estrangeiro, documentos_verificados=[], status=status, visto=nome_visto)
        return obj, id

    def find_solicitacao_para_passaporte(self, passaporte: str):
        self.cursor.execute("SELECT estrangeiro, visto, status FROM solicitacaoDeVisto WHERE estrangeiro=?", (passaporte,))
        rows = self.cursor.fetchall()
        if rows == []:
            return []
        return rows
