import sqlite3

class RelatorioDAO():
    def __init__(self):
        self.banco = sqlite3.connect('visaccess.db')
        self.cursor = self.banco.cursor()

    def relatorio_paises(self):
        print('entrou no dao de paises')
        # precisa mudar para where s.status = aprovado quando houver solicitações aprovadas
        self.cursor.execute("""
        SELECT e.pais as país, count(e.pais) as qtd_vistos
        FROM solicitacaoDeVisto s
        inner JOIN estrangeiro e
        on s.estrangeiro = e.passaporte
        where s.status = 'aprovado'
        GROUP BY e.pais HAVING COUNT(e.pais) > 1 ORDER BY count(e.pais) DESC
        """)
        rows = self.cursor.fetchall()
        return rows
    
    def relatorio_tipos_de_visto(self):
        self.cursor.execute("""
        SELECT visto as 'Visto', count(visto) as 'Nº de Solicitações'
        from solicitacaoDeVisto
        GROUP by visto ORDER by count(visto) desc
        """)
        rows = self.cursor.fetchall()
        return rows