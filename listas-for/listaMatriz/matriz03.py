matriz_base = [
    [1, 2],
    [3, 4]
]

fator = int(input("digite o fator de escala: "))

for linha in matriz_base:
    for i in range(len(linha)):
        linha[i] = linha[i] * fator

print(matriz_base)