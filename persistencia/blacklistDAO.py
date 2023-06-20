import sqlite3


class BlacklistDAO:

    def __init__(self):
        self.conn = sqlite3.connect("visaccess.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS blacklist (passaporte TEXT PRIMARY KEY NOT NULL, nome TEXT NOT NULL)')

    def close(self):
        self.conn.close()

    def create_tuple_blacklist(self, passaporte: str, nome: str):
        self.cursor.execute("INSERT INTO blacklist (passaporte, nome) VALUES (?, ?)", [passaporte, nome])
        self.conn.commit()

    def encontra_passaporte(self, passaporte: str):
        self.cursor.execute("SELECT * FROM blacklist WHERE passaporte=?", (passaporte,))
        row = self.cursor.fetchone()
        if row is None:
            return False
        return True

    def get_all_blacklist(self):
        self.cursor.execute("SELECT * FROM blacklist")
        rows = self.cursor.fetchall()
        blacklists = []
        for row in rows:
            blacklists.append({"nome": row[1], "passaporte": row[0]})
        return blacklists

    def delete_blacklist(self, passaporte: str):
        self.cursor.execute("DELETE FROM blacklist WHERE passaporte=?", [passaporte,])
        self.conn.commit()
