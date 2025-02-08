# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

while True:
    try:
        num_int1 = int(input("Digite o primeiro número inteiro positivo\n---> "))
        num_int2 = int(input("Digite o segundo número inteiro positivo\n---> "))
        num_int3 = int(input("Digite o terceiro número inteiro positivo\n---> "))
        num_int4 = int(input("Digite o quarto número inteiro positivo\n---> "))
        
        break
    except ValueError:
        # Captura erros de conversão (quando o usuário não insere o desejado)
        print("Desculpa, mas não é um número inteiro válido. Por favor, comece novamente.")
        

media = round((num_int1 + num_int2 + num_int3 + num_int4)/4, 2)

print(f"A média desses quatro números é: {media}")