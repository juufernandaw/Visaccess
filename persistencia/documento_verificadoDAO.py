import sqlite3


class DocumentoVerificadoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS documentoVerificado ('
                    'id_documento_verificado INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'preenchido TEXT NOT NULL,'
                    'id_solicitacao_visto INTEGER,'
                    'FOREIGN KEY (id_solicitacao_visto) REFERENCES solicitacaoDeVisto(id),'
                    'UNIQUE (id_documento_verificado, id_solicitacao_visto)'
                    ')')

    def close(self):
        self.conn.close()

    def create_documento_verificado(self, id_solicitacao_visto, preenchido):
        self.cursor.execute("INSERT INTO documentoVerificado (id_solicitacao_visto, preenchido) VALUES (?, ?)",
                            [id_solicitacao_visto, preenchido])
        self.conn.commit()
        return
