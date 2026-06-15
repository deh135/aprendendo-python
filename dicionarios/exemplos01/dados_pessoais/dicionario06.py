estoque = { "teclado": 15, "mouse": 22, "monitor": 8}

print(estoque)
atualizar_estoque = False
continuar = "s"
while continuar == "s":

    nome, quantidade = input("""digite o nome do produto que voce deseja e a quantidade separados por virgula: """)
    retorno = estoque.get(nome, "produto nao encontrado! ").split(",")

    for chave, valor in estoque.items():
        if valor == 0:
            print("estoque esgostado! ")
            continue
        if valor < int(quantidade):
            print("estoque insuficiente! ")
        else:
            estoque[chave] -= int(quantidade)
            atualiza_estoque = True

    if atualizar_estoque:
        print("estoque atualizado!")
        for chave, valor in estoque.items():
            print(f"{chave} : {valor}")

    continuar = input("quer continuar? [s/n]")[0].lower()