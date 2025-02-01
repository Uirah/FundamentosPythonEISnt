
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

ano = int(input("Digite um ano a descobrir se é bissexto: "))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano {ano} é bissexto :)\n")
else:
    print(f"O ano {ano} não é bissexto :( \n")