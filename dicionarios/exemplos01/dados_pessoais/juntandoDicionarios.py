carro1 = {
    "marca" : "Chevrolet",
    "modelo" : "Chevete",
    "ano" : 1998
}

carro2 = {
    "modelo" : "brasilia",
    "cor" : "amarelo",
    "placa" : "JPG4021"
}

carro_completo = {**carro1, **carro2} #cria novo dicionario com 2 valores

novo_carro = carro1 | carro2

print(f"novo carro:{novo_carro}\n")

print(f"carro completo{novo_carro}\n")

carro1.update(carro2) # atualiza dicionario
print(f"carro 1 atualizado com update: {carro1}")

carro1 |= carro2

print(f"carro 1 atualizado | : {carro1}")