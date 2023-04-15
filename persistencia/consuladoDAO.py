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

    def get_consulado_by_sede(self, sede):
        self.cursor.execute("SELECT * FROM consulado WHERE sede=?", sede)
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {'id': row[0], 'sede': row[1]}

    def delete_consulado(self, sede):
        self.cursor.execute("DELETE FROM consulado WHERE sede=?", sede)
        self.conn.commit()
