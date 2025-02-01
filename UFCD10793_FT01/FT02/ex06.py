
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** Fundamentos de Python *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")


tempFahr = float(input("Introduza uma temperatura em graus Fahrenheit:\n--->"))
tempCel = 5*(tempFahr-32)/9
if tempCel == 0 or tempCel == 1:
    print(f"Essa temperatura equivale a {5*(tempFahr-32)/9:.0f} grau Celsius\n")
else:
    print(f"Essa temperatura equivale a {5*(tempFahr-32)/9:.2f} graus Celsius\n")