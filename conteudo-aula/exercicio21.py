# exercicio 15: removendo duplicatas de um banco de dados

ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103]

lista_sem_duplicatas = []

for id in ids_clientes:
    if id not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(id)

print(lista_sem_duplicatas)