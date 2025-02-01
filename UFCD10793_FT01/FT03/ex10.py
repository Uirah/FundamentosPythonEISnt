
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

operacao = str(input("Digite qual operação queres utilizar: "))
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


if operacao == "+":
    print(f"A soma entre os dois valores é {valor1 + valor2} \n")
    
elif operacao == "-":
    if valor1 >= valor2:
        print(f"A diferença entre esses dois valores é {valor1 - valor2} \n")
    else:
        print(f"A diferença entre esses dois valores é {valor2 - valor1} \n")
    
elif operacao == "*":
    print(f"A multiplicação entre os dois valores é {valor1 * valor2} \n")
    
elif operacao == "/":
    if valor1 == 0 or valor2 == 0:
        print(f"A divisão com ZERO não é possível  :( \n")
        
    else:
        print(f"A divisão entre esses dois valores é {valor1 / valor2} \n")
    
else:
    print(f"Deu ruim :( \n")