while True:

    letra = input("digite uma letra (ou 0 para sair): ").lower()

    match letra:
        case "0":
            print("programa encerrado")
            break
        case "a"| "e"| "i"| "o"| "u":
            print("vogal")
        case _:
            print("consoante")