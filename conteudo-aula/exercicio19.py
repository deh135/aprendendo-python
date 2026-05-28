# exercicio 14: analise de desenpenho  de vendas

vendas = [120.50, 3400.00, 850.00, 5600.20, 2100.00, 850.00]

for i in range(6):
    valor = float(input("digite o valor da venda : "))
    vendas.append(valor)

media = sum(vendas) / len(vendas)

acima_media = []

for valor in vendas :
    if valor > media :
        acima_media.append(valor)

print("media das vendas: ", media)
print("vendas acima da media: ", acima_media)
