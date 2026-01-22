import sqlite3

conn = sqlite3.connect("nome_do_seu_banco.db")  # troque pelo seu .db
c = conn.cursor()

# Deleta a tabela de versionamento do Alembic
c.execute("DROP TABLE IF EXISTS alembic_version")

# Deleta todas as outras tabelas, se quiser resetar tudo
c.execute("DROP TABLE IF EXISTS usuarios")  # e outras que tiver

conn.commit()
conn.close()
print("Banco resetado!")
