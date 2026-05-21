ano_nascimento = int(input("qual o seu ano de nascimento?: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade < 18:
    print("menor de idade")
elif idade >= 60:
    print("idoso")
else:
    print("adulto")