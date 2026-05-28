# exercico 16: o tabuleiro de notas

turma = [
    ["ana", 8.0, 9,0],
    ["pedro", 5.5, 6.0],
    ["carlos", 7.5, 7.0] ]

for aluno in turma:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2

print(f"aluno(a) {nome} obteve media {media} ")