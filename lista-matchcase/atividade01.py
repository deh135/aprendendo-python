# exercicio 1: calculadora de dias da semana

while True:

    numero = int(input("Digite um numero de 1 a 7 ou 0 para sair: "))

    match numero:
       case 0:
            print("fim!")
            break
       case 1:
            print("domingo")
       case 2:
            print("segunda")
       case 3:
            print("terca-feira")
       case 4:
            print("quarta-feira")
       case 5:
            print("quinta-feira")
       case 6:
            print("sexta-feira")
       case 7:
            print("sabado")
       case _:
            print("invalido")