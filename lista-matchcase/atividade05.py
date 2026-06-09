# exercicio 5: validador de tipo de usuario e permissoes

while True:

    usuario =  input("digite seu usuario: ")
    match usuario:
        case "ADMIN" :
            print("acesso total: criar, ler, atualizar e deletar.")
        case "GERENTE" :
            print("acesso gerencial: criar, ler e atualizar.")
        case "EDITOR" :
            print("acesso de conteudo: ler e atualizar.")
        case "VISITANTE" :
            print("acesso restrito: apenas leitura.")
        case _:
            print("perfil não reconhecido. Acesso bloqueado.")