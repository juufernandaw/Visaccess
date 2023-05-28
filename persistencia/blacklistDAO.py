import sqlite3


class BlacklistDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS blacklist (passaporte TEXT PRIMARY KEY NOT NULL, nome TEXT NOT NULL)')

    def close(self):
        self.conn.close()

    def create_tuple_blacklist(self, passaporte, nome):
        self.cursor.execute("INSERT INTO blacklist (passaporte, nome) VALUES (?, ?)", [passaporte, nome])
        self.conn.commit()

    def encontra_passaporte(self, passaporte):
        self.cursor.execute("SELECT passaporte FROM blacklist WHERE passaporte=?", passaporte)
        row = self.cursor.fetchone()
        if row is None:
            return False
        return True
