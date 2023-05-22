import sqlite3
from entidades.solicitacao_de_visto import SolicitacaoDeVisto


class SolicitacaoDeVistoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS solicitacaoDeVisto (id integer PRIMARY KEY AUTO INCREMENT'
                            'data_solicitacao datetime PRIMARY KEY NOT NULL,'
                            'documentos_verificados TEXT FOREIGN KEY REFERENCES documento_verificado,'
                            'estrangeiro FOREIGN KEY REFERENCES estrangeiro,'
                            'status bool NOT NULL,'
                            'visto FOREIGN KEY REFERENCES TipoDeVisto)')

    def close(self):
        self.conn.close()

    def create_consulado(self, sede):
        self.cursor.execute("INSERT INTO consulado (sede) VALUES (?)", [sede])
        self.conn.commit()

    def get_all_consulados(self):
        self.cursor.execute("SELECT * FROM consulado")
        rows = self.cursor.fetchall()
        consulados = []
        for row in rows:
            consulado = Consulado(sede=row[0])
            consulados.append(consulado.sede)
        return consulados

    # def get_consulado_by_sede(self, sede):
    #     self.cursor.execute("SELECT * FROM consulado WHERE sede=?", sede)
    #     row = self.cursor.fetchone()
    #     if row is None:
    #         return None
    #     return {'sede': row[1]}

    def delete_consulado(self, sede):
        self.cursor.execute("DELETE FROM consulado WHERE sede=?", [sede])
        self.conn.commit()

    def update_consulado(self, nova_sede, velha_sede):
        self.cursor.execute(f"UPDATE consulado SET sede='{nova_sede}' WHERE sede=?", [velha_sede])
        self.conn.commit()