import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 3000 WHERE nome = 'Pedro Santos'")

#Selecionar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)

# Atualizar os salários em 5%
cursor.execute("UPDATE funcionarios SET salario = salario * 1.05")

#Selecionar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)

print()

conn.commit()
conn.close()