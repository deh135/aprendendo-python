nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
nota4 = float(input("digite sua quarto nota: "))

listaNotas = [nota1, nota2, nota3, nota4]

media = sum(listaNotas) / 4

print("sua media foi : ", media)

if media >= 7.0 :
    print("situacao: Aprovado")
else:
    print("situacao: Recuperacao")

print(*listaNotas)