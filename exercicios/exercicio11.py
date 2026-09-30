def listar_aprovados():
    print('Alunos aprovados:')

    with open('alunos2.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(';')
            nota = float(nota)

            if nota >= 6:
                print(f'{nome} - {nota}')


listar_aprovados()