
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade em anos: "))
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite altura em metros: "))

imc = round((peso/(altura*altura)), 2)

if imc < 17:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Muito abaixo do peso ideal \n")
elif 17 <= imc < 18.5:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Abaixo do peso \n")
    
elif 18.5 <= imc < 25:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Peso normal \n")
    
elif 25 <= imc < 30:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Acima do peso \n")
    
elif 30 <= imc < 35:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Obesidade I \n")
    
elif 35 <= imc < 40:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Obesidade II (severa)  \n")
    
elif 40 <= imc:
    print(f"{nome}, seu peso resulta em um IMC de {imc}, isso é considerado como: Obesidade III (mórbida) \n")

else:
    print(f"Deu ruim :( \n")