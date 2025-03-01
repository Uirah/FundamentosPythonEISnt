import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS funcionarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   cargo TEXT NOT NULL,
                   salario REAL NOT NULL
                )
                ''')

print("\nA tabela 'Empresa' foi criada com sucesso.\n")

conn.commit()
conn.close()
