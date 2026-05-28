# exercicio 11: caixa eletronico

valor = int(input("digite o valor do saque: "))

cedulas_50 = valor // 50
valor = valor % 50

cedulas_20 = valor // 20
valor = valor % 20

cedulas_10 = valor // 10
valor = valor % 10

cedulas_5 = valor // 5
valor = valor % 5

cedulas_2 = valor // 2
valor = valor % 2

print("cedulas de 50:", cedulas_50)
print("cedulas de 20:", cedulas_20)
print("cedulas de 10:", cedulas_10)
print("cedulas de 5:", cedulas_5)
print("cedulas de 2:", cedulas_2)