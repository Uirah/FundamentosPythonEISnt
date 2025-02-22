import csv

def cria_novo_ficheiro_csv():
    dados = [["Nome", "Idade", "Distrito"]]
    with open("dados.csv", "w", newline='', encoding="utf-8") as ficheiro:
        escritor = csv.writer(ficheiro)
        escritor.writerows(dados)

def adicionar_nova_pessoa():
    nova_pessoa = input("Qual o nome da nova pessoa: ")
    nova_idade = input("Qual é a idade dessa pessoa: ")
    novo_distrito = input("Qual é o Distrito da morada dessa pessoa: ")

        
    novos_dados = [[nova_pessoa, nova_idade, novo_distrito]]
    with open("dados.csv", "a", newline='', encoding="utf-8") as ficheiro:
        escritor = csv.writer(ficheiro)
        escritor.writerows(novos_dados) # Adiciona novas linhas sem apagar as existentes
        print("Nova pessoa adicionado com sucesso")


def imprimir_ficheiro():
    with open("dados.csv", newline='', encoding="utf-8") as ficheiro:
        leitor = csv.reader(ficheiro)
        count=0
        for linha in leitor:
            if count == 0:
                print(f"\033[1;32;40m\t{linha[0]}\t\t{linha[1]}\t{linha[2]}\033[m")
                count+=1
            else:
                print(f"\t{linha[0]}\t\t{linha[1]}\t{linha[2]}")#em ficheiro CSV
    
    
def main():
    
    cria_novo_ficheiro_csv()
    
    # Menu de operações
    while True:
        print("\n\t\033[1;32;47m***** Menu de Funções *****\033[m\n")
        print("\t1. Criar novo ficheiro CSV")
        print("\t2. Adicionar pessoa ao ficheiro CSV")
        print("\t3. Imprimir o ficheiro CSV")
        print("\t4. Sair")
        

        opcao = input("\nEscolha uma opção: ")
        
        match opcao:
            case "1":
                cria_novo_ficheiro_csv()
                print("Novo ficheiro criado.")
            case "2":
                adicionar_nova_pessoa()
            case "3":
                imprimir_ficheiro()
            case "4":
                print("A sair do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
    