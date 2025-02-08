# Importar o módulo cabecalho
from modulos import cabecalho

# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

while True:
    try:
        # Solicita o número do mês
        num_mes = int(input("Digite qual o número do mês que você nasceu: "))
        
        # Verifica se o número está entre 1 e 12
        match num_mes:
            case 1:
                print("Você nasceu em Janeiro. Que fixe!\n")
                break
            case 2:
                print("Você nasceu em Fevereiro. Que fixe!\n")
                break
            case 3:
                print("Você nasceu em Março. Que fixe!\n")
                break
            case 4:
                print("Você nasceu em Abril. Que fixe!\n")
                break
            case 5:
                print("Você nasceu em Maio. Que fixe!\n")
                break
            case 6:
                print("Você nasceu em Junho. Que fixe!\n")
                break
            case 7:
                print("Você nasceu em Julho. Que fixe!\n")
                break
            case 8:
                print("Você nasceu em Agosto. Que fixe!\n")
                break
            case 9:
                print("Você nasceu em Setembro. Que fixe!\n")
                break
            case 10:
                print("Você nasceu em Outubro. Que fixe!\n")
                break
            case 11:
                print("Você nasceu em Novembro. Que fixe!\n")
                break
            case 12:
                print("Você nasceu em Dezembro. Que fixe!\n")
                break
            case _:
                print("Desculpa, mas esse mês não faz parte do calendário grego-romano que usamos.")
    except ValueError:
        # Captura erros de conversão (quando o usuário não insere um número)
        print("Por favor, insira um número inteiro válido, entre 1 e 12.")