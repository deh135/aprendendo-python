"""" exercicio 9 """

while True:
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - sair")

    opcao = int(input("escolha uma opcao?"))

    if opcao ==  5:
        print("progama encerrado")
        break

    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))

    if opcao == 1:
        print("resultado: ", n1 + n2)

    elif opcao == 2:
        print("resultado: ", n1 - n2)

    elif opcao == 3:
       print("resultado: ", n1 * n2)

    elif opcao == 4:
        print("resultado: ", n1 / n2)

    else:
        print("opcao invalida")