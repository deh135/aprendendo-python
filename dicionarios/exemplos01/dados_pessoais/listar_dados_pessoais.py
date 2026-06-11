dados_pessoais = {
    "nome" : "Joao",
    "idade" : 17,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura": 170,
    "temCNH" : True
}

for chave, valor in dados_pessoais.items():
    print(f"{chave}:{valor}")

print("--------------------------------------------------")

# remove e retorna o valor removido ou o valor padrao
print( dados_pessoais.pop ("peso", "chave nao existe!" ) )
print( dados_pessoais.pop("nascimento", "chave nao existe! ") )
print( dados_pessoais.popitem() )

print("-----------------------------------------------------")
# como imprimir somente os valores
print( dados_pessoais.valor() )

print("----------------------------------------------------")
print("setando valor: ")
# seta um valor ou retorna um existente
print(
dados_pessoais.setdefault("peso", 80),
dados_pessoais.setdefault("telefone", "61999775"),
dados_pessoais.setdefault("idade", 25)
)

print(dados_pessoais.clear())
print(dados_pessoais)
