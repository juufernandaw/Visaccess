import psycopg2


# Conecta ao banco de dados PostgreSQL
conn = psycopg2.connect(
    # host="localhost",
    host="150.162.124.65",
    database="visaccess",
    user="postgres",
    # password="admin"
)

# Cria um cursor para executar comandos SQL
cur = conn.cursor()

# Executa um comando SQL
cur.execute("SELECT * FROM consulado")

# Obtém os resultados
results = cur.fetchall()

# Fecha o cursor e a conexão
cur.close()
conn.close()
