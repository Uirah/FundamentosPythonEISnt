kms = int(input("Digite quantos quilometros foram rodados: "))
litros = int(input("Digite quantos litros foram consumidos: "))

print(f"O consumo desse percurso foi {kms/litros}km/L ou {(litros/kms)*100:.2f}")