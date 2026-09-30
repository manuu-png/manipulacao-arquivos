def cadastrar_produtos():
    produtos = []

    with open('produtos.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(';')

            produto = {
                'nome': nome,
                'preco': float(preco),
                'quantidade': int(quantidade)
            }

            produtos.append(produto)

    print(produtos)


cadastrar_produtos()