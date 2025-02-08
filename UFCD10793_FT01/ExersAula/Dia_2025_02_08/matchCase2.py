
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

operacao = str(input("Digite qual operação queres utilizar: "))
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


match operacao:
    case "+":
        print(f"A soma entre os dois valores é {valor1 + valor2} \n")
    
    case "-":
        if valor1 >= valor2:
            print(f"A diferença entre esses dois valores é {valor1 - valor2} \n")
        else:
            print(f"A diferença entre esses dois valores é {valor2 - valor1} \n")
    
    case "*":
        print(f"A multiplicação entre os dois valores é {valor1 * valor2} \n")
    
    case "/":
        if valor2 == 0:
            print(f"A divisão por ZERO não é possível  :( \n")
        
        else:
            print(f"A divisão entre esses dois valores é {valor1 / valor2} \n")

    case _:
        print(f"Essa operação não é válida :( \n")