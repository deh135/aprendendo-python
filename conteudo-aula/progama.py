listaIdades = []
continuar = input("quer comecar a perguntar idade? (s/n) ").upper()[0]

while continuar == "S" or continuar == "C":
    idade = int(input("digite sua idade: "))
    listaIdades.append(idade)
    continuar = input("quer continuar? (s/n) ").upper()[0]

    print(listaIdades)