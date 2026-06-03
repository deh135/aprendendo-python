# exercicio 3: Menu de sistema de autoatendimento

while True:

    codigo = int(input("digite seu codigo:" ))
    match codigo:
        case 100:
            print("cachoro-quente - R$ 10,00")
        case 101:
            print("bauru simples - R$ 15,00")
        case 102:
            print("X-salada - R$ 15,00")
        case 103:
            print("Hamburguer - R$ 13,00")
        case _:
            print("codigo de produto invalido")