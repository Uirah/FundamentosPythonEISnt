'''Elabora uma script em python que peça ao utilizador dois números e devolva
a divisão do primeiro número introduzido pelo seguinte. Trate erros como
divisão por zero e valores inválidos.'''

try:
    a = int(input("\nDigite um número: "))
    b = int(input("Digite outro número: "))
    print(f"\nResultado da divisão do primeiro pelo segundo número é: {round(a/b,3)}\n")
        
except ZeroDivisionError:
    print("\nErro: Não é possível fazer divisão por zero.\n")

except ValueError:
    print("\nErro: Apenas números inteiros são permitidos.\n")
