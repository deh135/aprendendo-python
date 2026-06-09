senha_correta = "12345"

for tentativas in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_correta:
        print("Senha correta")
        break

else:
    print("conta bloqueada")