dados_pessoais = {
    "nome" : "joao",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura" : 1.70,
    "temCNH" : True
}

dados_pessoais["altura"] = 1.85
dados_pessoais["peso"] = 70
dados_pessoais.pop("idade") #remove o item


continuar = "s"
while continuar == "s":
    nova_chave, novo_valor = input("digite uma nova chave e um novo valor ou realize uma atualizacao de dados: ").split(
    ",")
    dados_pessoais[nova_chave] = novo_valor
    print(dados_pessoais.keys())

    dados = input("digite o que voce quer encontrar: ")

    print(dados_pessoais.get( dados, "valor nao encontrado! "))

    continuar = input("quer continuar? [s/n] ")[0].lower()