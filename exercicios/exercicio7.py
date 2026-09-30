def buscar_nome():
    lista_nomes = []

    with open('nomes.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_nomes.append(linha.strip())

    nome = input('Digite o nome que deseja pesquisar: ')

    if nome in lista_nomes:
        print('Nome encontrado!')
    else:
        print('Nome não encontrado!')


buscar_nome()