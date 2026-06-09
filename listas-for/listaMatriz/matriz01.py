matriz_quadrada = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6],
]

numeros = []
for i in range(len(matriz_quadrada)):
    numeros.append(matriz_quadrada[i][i])


print(f"a soma da diagonal da matriz quadrada de {"+".join(map(str, numeros))} = {sum(numeros)}")

print(map)