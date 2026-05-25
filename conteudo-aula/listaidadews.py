listaIdades = []
for i in range(18):
    idade = int(input("digite sua idade: "))
    listaIdades.append(idade)

print("-------------------------")
print("imprimindo idades uma abaixo da outra")
listaIdades.sort()

for i in listaIdades:
    print(i)