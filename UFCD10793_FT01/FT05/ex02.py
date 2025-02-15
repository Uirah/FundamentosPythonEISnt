# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

'''Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista;'''

def adicionar_inicio(lista, elemento):
    lista.insert(0, elemento)
    print(f"\nO elemento {elemento} foi adicionado no início da lista.")

def adicionar_fim(lista, elemento):
    lista.append(elemento)
    print(f"\nO elemento {elemento} foi adicionado no fim da lista.")
    
def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
        print(f"\nO elemento {elemento} foi removido da lista.")
    else:
        print(f"\nO elemento {elemento} não foi encontrado na lista.")
        
def tamanho_lista(lista):
    return print(f"\nO tamanho da lista é: {len(lista)}\n")

def imprimir_lista(lista):
    if lista:
        print(f"\nElementos da lista: {lista}")
    else:
        print("\nA lista está vazia.")
        
def esvaziar_lista(lista):
    lista.clear()
    print("\nA lista foi esvaziada.")
    
    
def main():
    lista = []

    # Menu de operações
    while True:
        print("\n\033[1;32;47m***** Menu de Funções *****\033[m\n")
        print("1. Adicionar elemento no início")
        print("2. Adicionar elemento no fim")
        print("3. Remover elemento")
        print("4. Ver tamanho da lista")
        print("5. Imprimir elementos da lista")
        print("6. Esvaziar lista")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                elemento = input("Digite o elemento a ser adicionado no início da lista: ")
                adicionar_inicio(lista, elemento)
            case "2":
                elemento = input("Digite o elemento a ser adicionado no fim da lista: ")
                adicionar_fim(lista, elemento)
            case "3":
                elemento = input("Digite o elemento a ser removido: ")
                remover_elemento(lista, elemento)
            case "4":
                tamanho_lista(lista)
            case "5":
                imprimir_lista(lista)
            case "6":
                esvaziar_lista(lista)
            case "7":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()