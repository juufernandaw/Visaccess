import sqlite3


class TipoVistoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        # self.cursor.execute('CREATE TABLE IF NOT EXISTS documentoVerificado (id_documento_verificado integer AUTO INCREMENT,'
        #                     'id_solicitacao_visto integer FOREIGN KEY REFERENCES solicitacaoDeVisto NOT NULL,'
        #                     'preenchido integer NOT NULL,'
        #                     'PRIMARY KEY(id_documento_verificado, id_solicitacao_visto))')

    def close(self):
        self.conn.close()

    def get_documentos_from_tipo_visto(self, id_tipo_visto: int):
        #  vai pegar um dado id de tipo de visto e retornar os documentos {"nome": nome, "id": id}
        return {"nome": nome, "id": id}
