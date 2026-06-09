estoque = [
    [12, 5, 8],
    [3, 15, 2],
    [19, 0, 7]
]

prateleira = int(input("digite o numero da prateleira (1 a 3): "))
divisoria = int(input("digite o numero da divisoria (1 a 3): "))

print("quantidade de caixas:", estoque [prateleira - 1][divisoria - 1])