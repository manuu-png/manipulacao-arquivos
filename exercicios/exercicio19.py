def gerar_relatorio():
    vendas = []

    with open('vendas.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(';')

            venda = {
                'vendedor': vendedor,
                'produto': produto,
                'valor': float(valor)
            }

            vendas.append(venda)

    total = 0
    quantidade_vendas = {}

    for venda in vendas:
        print(f"{venda['vendedor']} - {venda['produto']} - R$ {venda['valor']:.2f}")

        total += venda['valor']

        vendedor = venda['vendedor']

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print(f'\nTOTAL DE VENDAS: R$ {total:.2f}')

    print('\nQuantidade de vendas:')

    for vendedor, quantidade in quantidade_vendas.items():
        print(f'{vendedor}: {quantidade}')


gerar_relatorio()