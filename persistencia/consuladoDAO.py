import sqlite3
from entidades.consulado import Consulado


class ConsuladoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS consulado (sede TEXT PRIMARY KEY NOT NULL)')

    def close(self):
        self.conn.close()

    def create_consulado(self, sede: str):
        self.cursor.execute("INSERT INTO consulado (sede) VALUES (?)", [sede])
        self.conn.commit()

    def get_all_consulados(self):
        self.cursor.execute("SELECT * FROM consulado")
        rows = self.cursor.fetchall()
        consulados = []
        for row in rows:
            consulado = Consulado(sede=row[0])
            consulados.append(consulado.sede)
        return consulados

    def get_consulado_by_sede(self, sede: str):
        self.cursor.execute("SELECT * FROM consulado WHERE sede=?", [sede,])
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'sede': row}

    def delete_consulado(self, sede):
        self.cursor.execute("DELETE FROM consulado WHERE sede=?", [sede])
        self.conn.commit()

    def update_consulado(self, nova_sede: str, velha_sede: str):
        self.cursor.execute(f"UPDATE consulado SET sede='{nova_sede}' WHERE sede=?", [velha_sede])
        self.conn.commit()
