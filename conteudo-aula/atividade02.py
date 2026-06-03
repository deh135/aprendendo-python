# exercicio 2: conversor de notas em conceitos

while True:

    letra = input("Digite uma letra: ")
    match letra:
        case "A":
            print("Excelente trabalho!")
        case "B":
            print("Bom trabalho!")
        case"C":
            print("Satisfatorio")
        case "D":
            print("Abaixo da media(Atencao!)")
        case "E":
            print("Reprovado")
        case _:
            print("Conceito desconhecido")