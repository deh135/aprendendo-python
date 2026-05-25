listaAnos = []
for i in range (7):
    listaAnos.append(i)
anos = int(input("digite o ano que você nasceu: "))

anos = (anos - 2026)

if anos >= 18:
    print("Maior de Idade")
else:
    print("menor de idade")

print(*listaAnos)