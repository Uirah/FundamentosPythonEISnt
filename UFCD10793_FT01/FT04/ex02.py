# Importar o módulo cabecalho
from modulos import cabecalho

# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

while True:
    try:
        estado_civil = str(input("Digite seu estado civil\n(S) para Solteira(o)\n(C) para Casada(a)\n(V) para Viúva(o)\n---> ")).upper()
        
        match estado_civil:
            case "S":
                print("Podes então sair em uns encontros. Que fixe!\n")
                break
            case "C":
                print("Então tens alguém para dividir suas memórias. Que fixe!\n")
                break
            case "V":
                print("Que pena que não tens mais alguém para partilhar tua vida. :(\n")
                break
            case _:
                print("Desculpa, mas não é um estado civil válido.")
    except ValueError:
        # Captura erros de conversão (quando o usuário não insere o desejado)
        print("Por favor, insira S, C ou V.")