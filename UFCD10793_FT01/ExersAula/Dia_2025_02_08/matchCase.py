nome = input("Qual o nome do produto?\n---> ").lower()
preco = float(input("Qual o preço do produto?\n---> "))

match nome: 
    case "smartphone":
        preco_final = preco*0.9
        print(f"O preço final do smartphone será: {round(preco_final, 2)}€")
    case "tablet":
        preco_final = preco*0.85
        print(f"O preço final do tablet será: {round(preco_final, 2)}€")
    case "laptop":
        preco_final = preco*0.8
        print(f"O preço final laptop será: {round(preco_final, 2)}€")
    case _:
        print(f"O preço final desse produto não terá desconto, será: {preco}€")