import sqlite3


class EstrangeiroDAO:

    def __init__(self):
        # Create an in-memory SQLite database
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS estrangeiro (
                passaporte TEXT PRIMARY KEY,
                nome TEXT,
                data_nasc DATE,
                estado_civil TEXT
                pais TEXT
                estado TEXT
                cidade TEXT
                trabalho BOOLEAN
                profissao TEXT
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def cadastrar_estrangeiro(self, passaporte, nome, data_nasc, estado_civil, pais, estado, cidade, trabalho,
                              profissao):
        self.cursor.execute(
            "INSERT INTO estrangeiro (passaporte, nome, data_nasc, estado_civil, pais, estado, cidade, trabalho, profissao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (passaporte, nome, data_nasc, estado_civil, pais, estado, cidade, trabalho, profissao))
        self.conn.commit()

    def buscar_estrangeiro_por_passaporte(self, passaporte):
        self.cursor.execute("SELECT * FROM estrangeiro WHERE passaporte=?", (passaporte,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'passaporte': row[0]}

    def buscar_todos_estrangeiros(self):
        self.cursor.execute("SELECT * FROM estrangeiro")
        rows = self.cursor.fetchall()
        estrangeiros = []
        for row in rows:
            agente = {'passaporte': row[0], 'nome': row[1]}
            estrangeiros.append(agente)
        return estrangeiros

    def atualizar_estrangeiro(self, passaporte_antigo, passaporte_novo, nome, data_nasc, estado_civil, pais, estado,
                              cidade, trabalho, profissao):
        self.cursor.execute(
            "UPDATE estrangeiro SET passaporte=?, nome=?, data_nasc=?, estado_civil=?, pais=?, estado=?, cidade=?, trabalho=?, profissao=? WHERE passaporte=?",
            (passaporte_novo, nome, data_nasc, estado_civil, pais, estado, cidade, trabalho, profissao,
             passaporte_antigo))
        self.conn.commit()

    def excluir_estrangeiro(self, passaporte):
        self.cursor.execute("DELETE FROM estrangeiro WHERE passaporte=?", (passaporte,))
        self.conn.commit()

    # def encontra_passaporte(self, passaporte):
    #     # valida se tem estrangeiro com tal passaporte
    #     if passaporte_encontrado:
    #         return True
    #     else:
    #         return False
