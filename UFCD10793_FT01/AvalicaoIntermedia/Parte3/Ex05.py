import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Eliminar Mariana Costa
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Mariana Costa'")

#Selecionar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)

print()

# Eliminar Mariana Costa
cursor.execute("DELETE FROM funcionarios WHERE salario < 3000")

#Selecionar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)
    
print()

conn.commit()
conn.close()