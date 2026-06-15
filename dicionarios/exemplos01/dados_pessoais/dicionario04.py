produtos = {
    "arroz carreteioro" : 25.50,
    "feijoada" : 10.50,
    "macarrao" : 15.79
}

produto = input("digite o nome do produto: ")

if produto in produtos:
    print("preco: ", produtos[produto])
else:
    print("produto nao encontrado!")