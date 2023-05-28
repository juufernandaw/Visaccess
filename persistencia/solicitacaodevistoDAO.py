import sqlite3


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

    def create_solicitacao_visto(self, data_solicitacao, passaporte_estrangeiro, status, id_visto):
        self.cursor.execute("INSERT INTO solicitacaoDeVisto (data_solicitacao, estrangeiro, status, visto) VALUES (?, ?, ?, ?)",
                            [data_solicitacao, passaporte_estrangeiro, status, id_visto])
        self.conn.commit()
        return id  # id pk da solicitacaodevisto criada

    def find_solicitacao_para_passaporte(self, passaporte: str):
        self.cursor.execute("SELECT estrangeiro, visto, status FROM solicitacaoDeVisto WHERE estrangeiro=?", passaporte)
        rows = self.cursor.fetchall()
        if rows is None:
            return []
        return rows
