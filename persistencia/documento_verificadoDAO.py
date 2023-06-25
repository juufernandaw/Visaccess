import sqlite3
from entidades.documento_verificado import DocumentoVerificado
from entidades.documento import Documento


class DocumentoVerificadoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS documentoVerificado ('
                    'documento TEXT,'
                    'preenchido INTEGER NOT NULL,'
                    'id_solicitacao_visto INTEGER,'
                    'FOREIGN KEY (id_solicitacao_visto) REFERENCES solicitacaoDeVisto(id),'
                    'FOREIGN KEY (documento) REFERENCES documento(nome),'
                    'PRIMARY KEY (documento, id_solicitacao_visto)'
                    ')')

    def close(self):
        self.conn.close()

    def create_documento_verificado(self, id_solicitacao_visto, preenchido, documento):
        self.cursor.execute("INSERT INTO documentoVerificado (id_solicitacao_visto, documento, preenchido) VALUES (?, ?, ?)",
                            [id_solicitacao_visto, documento, preenchido])
        self.conn.commit()
        self.cursor.execute("SELECT regra FROM documento WHERE nome=?", (documento,))
        row = self.cursor.fetchone()
        preenchido = True if preenchido == 1 else False
        print("Instanciando documento e documento verificado")
        doc = Documento(nome=documento, regra=row)
        doc_verificado = DocumentoVerificado(documento=doc, preenchido=preenchido)
        return doc_verificado

    def buscar_documentos_por_solicitacao(self, id_solicitacao):
        self.cursor.execute("SELECT documento, preenchido FROM documentoVerificado WHERE id_solicitacao_visto=?", (id_solicitacao,))
        rows = self.cursor.fetchall()

        return rows
