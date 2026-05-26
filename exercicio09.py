maiores = 0
menores = 0

for i in range(7):
    ano = int(input('digite o ano de nascimento: '))
    idade = 2026 - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('maiores: ', maiores)
print('menores: ', menores)