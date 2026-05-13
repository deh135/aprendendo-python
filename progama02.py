#Atividade de media

frequencia = int(input("informe quantos dias o aluno compareceu as aulas : "))

if frequencia > 0 :
    nota1 = float(input("digite a sua primeira nota").replace ("," , "."))
    nota2 = float(input("digite a sua segunda nota").replace ("," , "."))

    media = (nota1 + nota2) / 2

    if media >= 7 :
        print("APROVADO")
    elif media>=5:
        print("RECUPERACAO")
    elif media < 5 : 
        print("REPROVADO")
else:
    print("aluno nao foi as aulas")