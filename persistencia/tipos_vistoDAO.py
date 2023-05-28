import sqlite3


class Tipos_VistoDAO:
    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tipos_visto (
                name TEXT PRIMARY KEY,
                validade DATE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visa_documents (
                visa_name TEXT,
                nomedoc TEXT,
                FOREIGN KEY (visa_name) REFERENCES tipos_visto(name),
                FOREIGN KEY (nomedoc) REFERENCES documento(nome)
            )
        ''')
        self.conn.commit()

    def cadastrar_tipos_visto(self, nome, date):
        self.cursor.execute("INSERT INTO tipos_visto (name, validade) VALUES (?, ?)", (nome, date))
        self.conn.commit()

    def cadastrar_documentos_para_visto(self, docs, visa_name):
        for doc in docs:
            self.cursor.execute("INSERT INTO visa_documents (visa_name, nomedoc) VALUES (?, ?)",
                                (visa_name, doc['nomedoc']))
            self.conn.commit()

    def buscar_todos_tipos_visto(self):
        self.cursor.execute("SELECT * FROM tipos_visto")
        rows = self.cursor.fetchall()
        tipos = []
        for row in rows:
            visto = {'nome': row[0], 'data': row[1]}
            tipos.append(visto)
        return tipos

    def buscar_visto_por_nome(self, nome):
        self.cursor.execute("SELECT * FROM tipos_visto WHERE name=?", (nome,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'nome': row[0], 'date': row[1]}

    def buscar_documentos_por_visto(self, visa_name):
        self.cursor.execute('''
            SELECT nomedoc
            FROM visa_documents
            JOIN tipos_visto ON visa_documents.visa_name = tipos_visto.name
            WHERE tipos_visto.name = ?
        ''', (visa_name,))
        results = self.cursor.fetchall()
        documents = [result[0] for result in results]
        return documents

    def excluir_visto(self, nome):
        self.cursor.execute("DELETE FROM tipos_visto WHERE name=?", (nome,))
        self.conn.commit()

    def excluir_relacao_visto_documento(self, visa_name):
        self.cursor.execute("DELETE FROM visa_documents WHERE visa_name=?", (visa_name,))
        self.conn.commit()

    def atualizar_visto(self, nome_antigo, nome_novo, data):
        # Atualiza o CPF, nome, senha e consulado na tabela 'agentes'
        self.cursor.execute("UPDATE tipos_visto SET name=?, date=? WHERE name=?", (nome_novo, data, nome_antigo))

    # def get_documentos_from_tipo_visto(self, id_tipo_visto: int):
    #     #  vai pegar um dado id de tipo de visto e
    #     #  ai vai validar na tabela associativa de docs e tipos de vistos
    #     #  e retornar os documentos atrelados a ao tipo de visto em formato de lista de dicts {"nome": nome, "id": id}
    #     return list[dict, dict,...]
    #
    # def get_all_tipos_visto(self):
    #     # aqui vai fazer uma busca na tabela tipos de visto
    #     # e depois vai transformar em dicts e colocar em uma lista composta por dicts
    #     return list[dict, dict,...]