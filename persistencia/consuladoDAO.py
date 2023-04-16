import sqlite3


class ConsuladoDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS consulado (id INTEGER AUTOINCREMENT, sede TEXT PRIMARY KEY)')

    def close(self):
        self.conn.close()

    def create_consulado(self, sede):
        self.cursor.execute("INSERT INTO consulado (sede) VALUES (?)", sede)
        self.conn.commit()

    def get_all_consulados(self):
        self.cursor.execute("SELECT * FROM consulado")
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'id': row[0], 'sede': row[1]}

    def get_consulado_by_sede(self, sede):
        self.cursor.execute("SELECT * FROM consulado WHERE sede=?", sede)
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'id': row[0], 'sede': row[1]}

    def delete_consulado(self, sede):
        self.cursor.execute("DELETE FROM consulado WHERE sede=?", sede)
        self.conn.commit()

    def update_consulado(self, nova_sede, velha_sede):
        self.cursor.execute(f"UPDATE consulado SET sede={nova_sede} WHERE sede=?", velha_sede)
        self.conn.commit()
