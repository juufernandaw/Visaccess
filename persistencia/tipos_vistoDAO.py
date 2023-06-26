import sqlite3


class Tipos_VistoDAO:
    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tipos_visto (
                name TEXT PRIMARY KEY,
                validade INTEGER
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

    def cadastrar_tipos_visto(self, nome, years):
        self.cursor.execute("INSERT INTO tipos_visto (name, validade) VALUES (?, ?)", (nome, years))
        self.conn.commit()

    def cadastrar_documentos_para_visto(self, docs, visa_name):
        for doc in docs:
            print("concatenadndo")
            print(doc['nome'], visa_name)
            self.cursor.execute("INSERT INTO visa_documents (visa_name, nomedoc) VALUES (?, ?)",
                                (visa_name, doc['nome']))
            self.conn.commit()

    def buscar_todos_tipos_visto(self):
        self.cursor.execute("SELECT * FROM tipos_visto")
        rows = self.cursor.fetchall()
        tipos = []
        for row in rows:
            visto = {'nome': row[0], 'validade': row[1]}
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
            WHERE visa_name = ?
        ''', (visa_name,))
        results = self.cursor.fetchall()
        print(results)
        documents = [result[0] for result in results]
        return documents

    def excluir_visto(self, nome):
        self.cursor.execute("DELETE FROM tipos_visto WHERE name=?", (nome,))
        self.conn.commit()

    def excluir_relacao_visto_documento(self, visa_name):
        self.cursor.execute("DELETE FROM visa_documents WHERE visa_name=?", (visa_name,))
        self.conn.commit()

    def atualizar_visto(self, nome_antigo, nome_novo, years):
        # Atualiza o CPF, nome, senha e consulado na tabela 'agentes'
        self.cursor.execute("UPDATE tipos_visto SET name=?, validade=? WHERE name=?", (nome_novo, years, nome_antigo))
