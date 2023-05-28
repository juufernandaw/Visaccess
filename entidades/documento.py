import sqlite3
from telas.telaconsul import TelaConsul


class Documento:

    def __init__(self):
        self.__tela_consul = TelaConsul()
        self.banco = sqlite3.connect('documentos_tipo_de_visto.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos_tipo_de_visto (
                nome TEXT NOT NULL,
                regra TEXT NOT NULL
        );
        """)

    def registra_documento(self, nome: str, regra: str):
        self.cursor.execute("INSERT INTO documentos_tipo_de_visto (nome, regra) VALUES (?, ?)", [nome, regra])
        self.banco.commit()
        self.__tela_consul.exibe_mensagem_sucesso('Documento Cadastrado com Sucesso!')

    def lista_all_documentos(self):
        self.cursor.execute("SELECT * FROM documentos_tipo_de_visto")
        rows = self.cursor.fetchall()
        documentos = []
        for row in rows:
            documento = {'nome': row[0], 'regra': row[1]}
            documentos.append(documento)
        return documentos

    def localiza_documento_pelo_nome(self, nome: str):
        for documento in self.lista_all_documentos():
            if nome == documento['nome']:
                print('entrou no true')
                return True
        else:
            print('entrou no false')
            return False
    
    def remove_documento(self, nome: str):
        self.cursor.execute("DELETE FROM documentos_tipo_de_visto WHERE nome=?", [nome])
        self.banco.commit()
        
    def altera_documento(self, novo_nome, nova_regra, velho_nome):
        print('entrou no altera_documento')
        self.cursor.execute(f"UPDATE documentos_tipo_de_visto SET nome='{novo_nome}', regra='{nova_regra}' WHERE nome=?", [velho_nome])
        self.banco.commit()