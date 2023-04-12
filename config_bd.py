import psycopg2

conn = psycopg2.connect(
    host="192.168.0.35",
    database="visaccess",
    user="postgres",
)

# Cria um cursor para executar comandos SQL
cur = conn.cursor()

# Executa um comando SQL
cur.execute("SELECT * FROM consulado")

# Obtém os resultados
results = cur.fetchall()

cur.close()
conn.close()
