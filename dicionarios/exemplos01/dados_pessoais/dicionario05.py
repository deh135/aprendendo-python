frase = "joao tem vinte anos e joao tem vinte livros e os livros tem folhas pretas".split()

palavras = {"joao" : 2,
            "tem" : 3,
            "vinte" : 2,
            "anos" : 1,
            "e" : 1,
            "livros" : 2,
            "os" : 1,
            "pretas" : 1,
            "folhas" : 1

                    }

contagem = { }

for i in frase:
    if i not in contagem:
        contagem [i] = 1
    else:
        contagem[i] += 1