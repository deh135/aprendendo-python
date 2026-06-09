oceano = [
    ["~", "~", "~", "~"],
    ["~", "~", "N", "~"],
    ["~", "~", "~", "~"],
    ["~", "~", "~", "~"]
]

posicao = input("digite um numero: ")

linha, coluna = posicao.split(".")

linha = int(linha)
coluna = int(coluna)

if oceano[linha][coluna] == "N":
    print("voce afundou o navio! ")
else:
    print("agua!")