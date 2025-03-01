import sqlite3

def adicionar_funcionario(nome, cargo, salario):
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))


def listar_funcionarios():
    #Selecionar todos os funcionários
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    
    #Exibir os funcionários
    for funcionario in funcionarios:
        print(funcionario)
    print()
    
    
def atualizar_salario(novo_salario, nome):
    cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))

        
def eliminar_funcionario(nome):
    cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
    
    
def main():

    # Menu de operações
    while True:
        print("\n\033[1;32;47m***** Menu de Gestão de Funcionários *****\033[m\n")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Atualizar salário")
        print("4. Eliminar funcionário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                nome = input("Nome: ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                adicionar_funcionario(nome, cargo, salario)
                
            case "2":
                listar_funcionarios()
                
            case "3":
                nome = input("Nome: ")
                novo_salario = float(input("Salário: "))
                atualizar_salario(novo_salario, nome)
            case "4":
                nome = input("Nome: ")
                eliminar_funcionario(nome)
            case "5":
                conn.commit()
                conn.close()
                print("A sair do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    main()