from entidades.gerente import Gerente
import sqlite3

class GerenteDAO():
    def __init__(self):
        self.banco = sqlite3.connect('visaccess.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gerente (
                cpf INTEGER NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                consulado TEXT NOT NULL
        );
        """)

    def cria_gerente(self, gerente: Gerente): # adiciona novos dados na tabela
        print(f"gerente['cpf']: {gerente.cpf}")
        self.cursor.execute("INSERT INTO gerente (cpf, nome, senha, consulado) VALUES (?, ?, ?, ?)", [gerente.cpf, gerente.nome, gerente.senha, gerente.consulado])
        self.banco.commit()

    def lista_gerentes(self): # lista os dados da tabela
        self.cursor.execute("SELECT * FROM gerente")
        rows = self.cursor.fetchall()
        gerentes = []
        for row in rows:
            gerente = {'cpf': row[0], 'nome': row[1], 'senha': row[2], 'consulado': row[3]}
            gerentes.append(gerente)
        print(f"linhas tabela: {rows}")
        return gerentes

    def buscar_gerente_por_cpf(self, cpf):
        self.cursor.execute(f"SELECT * FROM gerente WHERE cpf = {cpf}")
        row = self.cursor.fetchone()
        if row is not None:
            cpf, nome, senha, consulado = row
            gerente = Gerente(cpf=cpf, nome=nome, senha=senha, consulado=consulado)
            return gerente
        else:
            return None
        
    def atualizar_gerente(self, gerente_novo, cpf_antigo):
        self.cursor.execute("UPDATE gerente SET cpf=?, nome=?, senha=?, consulado=? WHERE cpf=?", (gerente_novo['cpf'], gerente_novo['nome'], gerente_novo['senha'], gerente_novo['consulado'], cpf_antigo))
        self.banco.commit()
        
    def remover_gerente(self, gerente: Gerente): # remove dados da tabela
        try:
            print(f"gerente bd: {gerente}")
            print(f"gerente bd: {gerente['cpf']}")
            self.cursor.execute("DELETE from gerente WHERE cpf = ?", [gerente['cpf']])
            self.banco.commit()
            print("Dados excluídos com sucesso")
        except sqlite3.Error as erro:
            print("Erro ao excluir: ", erro)

