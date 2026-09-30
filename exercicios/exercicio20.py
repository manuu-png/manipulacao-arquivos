def carregar_alunos():
    alunos = []

    with open('alunos3.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_aluno, nome, idade, curso = linha.strip().split(';')

            aluno = {
                'id': int(id_aluno),
                'nome': nome,
                'idade': int(idade),
                'curso': curso
            }

            alunos.append(aluno)

    return alunos


def salvar_alunos(alunos):
    with open('alunos3.txt', 'w', encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['id']};"
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['curso']}\n"
            )


def listar_alunos(alunos):
    for aluno in alunos:
        print(f"{aluno['id']} - {aluno['nome']} - {aluno['idade']} anos")


def buscar_aluno(alunos):
    id_busca = int(input('Digite o ID: '))

    for aluno in alunos:
        if aluno['id'] == id_busca:
            print('Aluno encontrado:')
            print(aluno['nome'])
            print(f"{aluno['idade']} anos")
            print(aluno['curso'])
            return

    print('Aluno não encontrado!')


def cadastrar_aluno(alunos):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    curso = input('Curso: ')

    if len(alunos) > 0:
        novo_id = alunos[-1]['id'] + 1
    else:
        novo_id = 1

    aluno = {
        'id': novo_id,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }

    alunos.append(aluno)
    salvar_alunos(alunos)

    print('Aluno cadastrado com sucesso!')


def remover_aluno(alunos):
    id_remover = int(input('Digite o ID do aluno que deseja remover: '))

    for aluno in alunos:
        if aluno['id'] == id_remover:
            alunos.remove(aluno)
            salvar_alunos(alunos)

            print('Aluno removido com sucesso!')
            return

    print('Aluno não encontrado!')


def alterar_aluno(alunos):
    id_alterar = int(input('Digite o ID do aluno que deseja alterar: '))

    for aluno in alunos:
        if aluno['id'] == id_alterar:
            aluno['nome'] = input('Novo nome: ')
            aluno['idade'] = int(input('Nova idade: '))
            aluno['curso'] = input('Novo curso: ')

            salvar_alunos(alunos)

            print('Aluno alterado com sucesso!')
            return

    print('Aluno não encontrado!')


def sistema_alunos():
    alunos = carregar_alunos()

    while True:
        print('\n===== SISTEMA DE ALUNOS =====')
        print('1 - Listar alunos')
        print('2 - Buscar aluno')
        print('3 - Cadastrar aluno')
        print('4 - Remover aluno')
        print('5 - Alterar aluno')
        print('6 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            listar_alunos(alunos)

        elif opcao == '2':
            buscar_aluno(alunos)

        elif opcao == '3':
            cadastrar_aluno(alunos)

        elif opcao == '4':
            remover_aluno(alunos)

        elif opcao == '5':
            alterar_aluno(alunos)

        elif opcao == '6':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida!')


sistema_alunos()