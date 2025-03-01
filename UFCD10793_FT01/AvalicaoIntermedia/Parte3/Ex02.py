import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 1300)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 870)")

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Fernando Santos', 'Segurança', 1000)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Maria Pacheco', 'Limpeza', 870)")


conn.commit()
conn.close()