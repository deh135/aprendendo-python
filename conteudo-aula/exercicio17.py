# execicio 12:  analise de dados

mais_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input("digite a idade: "))
    sexo = input("digite o seu sexo (M/F):").upper()

    if idade > 18:
        mais_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

    continuar = input("deseja continuar? (S/N): ").upper()

    if continuar == "N":
        break

print("pessoas com mais de 18: ", mais_18)
print("homens cadastrados: ", homens)
print("mulheres com menos de 20: ", mulheres_menos_20)