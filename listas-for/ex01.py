listaNumeros = []

for i in range(1,7):
    numero = int(input(f"digite o {i}° numero:"))
    listaNumeros.append(numero)

listaNumeros.sort()
print(listaNumeros)

print(f"a soma e : {sum(listaNumeros)}")
print(f"o maior numero e : {max(listaNumeros)}")
print(f"o menor numero e: {min(listaNumeros)}")