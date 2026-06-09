# exercicio 4: o verificador de estacoes do ano

while True:

    mes = input("digite um mes do ano: ")
    match mes:
        case "janeiro" | "fevereiro" | "marco" | "1" | "2" | "3" :
            print("verão")
        case "abril" | "maio" | "junho" | "4" | "5" | "6" :
            print("outono")
        case "julho" | "agosto" | "setembro" | "7" | "8" | "9" :
            print("inverno")
        case "outubro" | "novembro" | "dezembro" | "10" | "11" | "12" :
            print("outono")
        case _:
            print("invalido")
