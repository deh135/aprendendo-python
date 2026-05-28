# carrinho de compras

carrinho = []

while True:
    produto = input("digite o produto(ou 'sair'): ")
    if produto.lower() == "sair":
        break
    carrinho.append(produto)
carrinho.sort()

print("produtos do carrinho: ")
print(carrinho)