import sqlite3

#Conectar à base de dados
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

#Selecionar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)

print()

#Fechar a conexão
conexao.close()