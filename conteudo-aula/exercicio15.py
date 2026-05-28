# exercicio 10: jog da adivinhacao

import random

numero_secreto = random.randint (1,20)

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("digite um numero de 1 a 20: "))
    if palpite < numero_secreto:
        print(" o numero secreto e maior!" )
    elif palpite > numero_secreto:
        print("o numero secreto e maior!" )
print("parabens! você acertou! ")