def carregar_nomes():
    lista_nomes = []

    with open('nomes.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_nomes.append(linha.strip())

    print(lista_nomes)


carregar_nomes()