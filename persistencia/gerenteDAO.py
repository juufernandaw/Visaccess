from entidades.gerente import Gerente
import sqlite3

class GerenteDAO():
    def __init__(self):
        self.banco = sqlite3.connect('gerente.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gerente (
                cpf INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                consulado TEXT NOT NULL
        );
        """)

    def add(self, gerente: Gerente): # adiciona novos dados na tabela
        self.cursor.execute(f"INSERT INTO gerente VALUES ({gerente.cpf, gerente.nome, gerente.senha, gerente.consulado})")
        self.cursor.commit()
        print(self.cursor.fetchall())
        self.banco.close()

    def get(self): # lista os dados da tabela
        self.cursor.execute("SELECT * FROM gerente")
        rows = self.cursor.fetchall()
        gerentes = []
        for row in rows:
            gerente = Gerente(sede=row[1])
            gerentes.append(gerente.sede)
        print(rows)
        return gerentes

    def remove(self, gerente: Gerente): # remove dados da tabela
        try:
            self.cursor.execute(f"DELETE from gerente WHERE cpf = {gerente.cpf}")
            self.banco.close()
            print("Dados excluídos com sucesso")
        except sqlite3.Error as erro:
            print("Erro ao excluir: ", erro)

    def buscar_gerente_por_cpf(self, cpf):
        self.cursor.execute(f"SELECT * FROM gerente WHERE cpf = {cpf}")
        row = self.cursor.fetchone()
        if row is not None:
            cpf, nome, senha, consulado = row
            gerente = Gerente(cpf=cpf, nome=nome, senha=senha, consulado=consulado)
            return gerente
        else:
            return None
