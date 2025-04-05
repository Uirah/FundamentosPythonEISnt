"""Escreve uma função em Python que dada uma lista de números imprime a soma dos
valores dessa lista, o número de elementos da lista e a media desses valores. Implementa
tratamento de exceções no teu código (try…except…else..finally)."""

def contas(numeros):
    try:
    
        for num in numeros:
            if not isinstance(num, (int, float)):
                raise ValueError("A lista deve conter apenas números.")
        
        soma = 0
        contagem = 0
        for num in numeros:
            contagem += 1
            soma += num
        
        if contagem > 0:
            media = soma / contagem
        else:
            media = 0
        
    except ValueError as e:
        print(f"Erro: {e}")
    except ZeroDivisionError:
        print("Erro: A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
    else:
        print(f"\nSoma dos valores: {soma}\nNúmero de elementos: {contagem}\nMédia dos valores: {round(media, 2)}")
        
    finally:
        print("\nCálculos concluídos. :)\n")

def main():
    numeros = [1,5,6,8,77,11,55,6,8,9]
    contas(numeros)


if __name__ == "__main__":
    main()
    
    
    

