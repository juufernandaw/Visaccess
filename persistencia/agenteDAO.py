import sqlite3


class AgenteDAO:

    def __init__(self):
        # Create an in-memory SQLite database
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS agente (
                cpf TEXT PRIMARY KEY,
                nome TEXT,
                senha INTEGER,
                consulado INTEGER
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def cadastrar_agente(self, cpf, nome, senha, consulado):
        self.cursor.execute("INSERT INTO agente (cpf, nome, senha, consulado) VALUES (?, ?, ?, ?)", (cpf, nome, senha, consulado))
        self.conn.commit()

    def buscar_agente_por_cpf(self, cpf):
        self.cursor.execute("SELECT * FROM agente WHERE cpf=?", (cpf,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'cpf': row[0], 'nome': row[1], 'senha': row[2], 'consulado': row[3]}

    def buscar_todos_agentes(self):
        self.cursor.execute("SELECT * FROM agente")
        rows = self.cursor.fetchall()
        agentes = []
        for row in rows:
            agente = {'cpf': row[0], 'nome': row[1], 'senha': row[2], 'consulado': row[3]}
            agentes.append(agente)
        return agentes
    
    def atualizar_agente(self, cpf_antigo, cpf_novo, nome, senha, consulado):
        # Atualiza o CPF, nome, senha e consulado na tabela 'agentes'
        self.cursor.execute("UPDATE agente SET cpf=?, nome=?, senha=?, consulado=? WHERE cpf=?", (cpf_novo, nome, senha, consulado, cpf_antigo))
        self.conn.commit()

    def excluir_agente(self, cpf):
        self.cursor.execute("DELETE FROM agente WHERE cpf=?", (cpf,))
        self.conn.commit()
