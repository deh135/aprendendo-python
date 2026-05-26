lista = []
pares = []
impares = []

contador = 0

while contador < 10:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    contador += 1

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("lista principal: ", lista)
print("pares: ", pares)
print("impares: ", impares)