import random as r


def gerador_id():
    fonte = 'ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789'
    sorteio = []
    for i in range(3):
        sorteio.append(r.choice(fonte))
    return ''.join(sorteio)


def menu():
    print('''    ------------------------------------
    |**        MENU DE OPÇÕES        **|
    |----------------------------------|
    | [1] - Inserir novo contato       |
    | [2] - Excluir contato            |
    | [3] - Excluir todos os contatos  |
    | [4] - Buscar contato             |
    | [5] - Listar todos os contatos   |
    | [6] - Sair da agenda             |
    ------------------------------------''')


def opcao_usuario():
    while True:
        try:
            entrada = int(input('    | Digite sua opção: '))
            return entrada
        except ValueError:
            print('    >>> Apenas números são permitidos! <<<')
            continue


def menu_principal():
    opcoes = [1, 2, 3, 4, 5, 6]
    op_selecionada = 0
    while op_selecionada not in opcoes:
        menu()
        op_selecionada = opcao_usuario()
        if op_selecionada not in opcoes:
            print('    >>> Opção inválida! Escolha novamente! <<<')
            input('    >>> Pressione ENTER para continuar...  <<<')
    return op_selecionada


def adicionar_novo():
    confirmacao = '?'
    dados_contato = None

    while confirmacao != 'y':
        dados_contato = recebe_dados()
        confirmacao = input('''    ------------------------------------
    | Pressione ou "y" para salvar os dados
    | ou qualquer tecla para digitar novamente: ''').lower()
        for i in range(10):
            print('')

    novo_id = gerador_id()

    while novo_id in contatos.keys():
        novo_id = gerador_id()

    contatos[novo_id] = dados_contato

    print('''    -----------------------------------------
    | ** Contato adicionado com sucesso! ** |
    -----------------------------------------''')

    repetir = input('''    | Pressione "n" para repetir a função ou 
    | qualquer tecla para retornar ao menu: ''').lower()
    if repetir == 'n':
        return adicionar_novo()


def recebe_dados():
    dados = []
    print('''    ------------------------------------
    |    Adicionando novo contato...   |
    ------------------------------------''')
    dados.append(input('    | Nome: '))
    dados.append(input('    | Telefone: '))
    dados.append(input('    | E-mail: '))
    return dados


def excluir_contato():
    print('''    -------------------------------------
    |        Excluindo contato...       |
    -------------------------------------''')
    id_para_excluir = input('    | Digite o ID do contato que deseja excluir: ').upper()
    if id_para_excluir not in contatos.keys():
        print('    | Contato não encontrado... ')
        repetir = input('''    | Pressione "y" para digitar novamente ou
    | qualquer tecla para retornar ao menu principal: ''').lower()
        if repetir == 'y':
            return excluir_contato()
    else:
        contatos.pop(id_para_excluir)
        print('    | Contato excluído com sucesso!')
        input('    | Pressione qualquer tecla para retornar ao menu principal...')


def excluir_todos():
    print('''    ------------------------------------
    |  Excluindo todos os contatos...  |
    ------------------------------------''')
    decisao_final = input('''    | Tem certeza disso?
    | Pressione "y" para prosseguir ou
    | Pressione qualquer tecla para desistir''').lower()
    if decisao_final == 'y':
        contatos.clear()
        input('''    ------------------------------------
    | Todos os contatos foram excluídos com sucesso!
    | Pressione qualquer tecla para retornar ao menu principal... ''')
    else:
        input('''    ------------------------------------
    | Nenhum contato foi excluído.
    | Pressione qualquer tecla para retornar ao menu principal... ''')


def buscar_contato():
    print('''    ------------------------------------
    |  Buscando dados do contato...  |
    ------------------------------------''')
    id_contato = input('    | Informe o ID do contato: ').upper()
    if id_contato not in contatos.keys():
        print('    | Contato não encontrado... ')
        repetir = input('''    | Pressione "y" para digitar novamente ou
    | qualquer tecla para retornar ao menu principal: ''').lower()
        if repetir == 'y':
            return buscar_contato()
    else:
        print('    | Contato encontrado!')
        print(f'    ------------------------------------')
        print(f'    | Nome: {contatos[id_contato][0]}')
        print(f'    | Telefone: {contatos[id_contato][1]}')
        print(f'    | Email: {contatos[id_contato][2]}')
        print(f'    ------------------------------------')
        input('    | Pressione qualquer tecla para retornar o menu principal...')


def listar_contatos():
    print('''    ------------------------------------
    |  Listando todos os contatos...  |
    ------------------------------------''')
    print(f'    | Total de contatos existentes: {len(contatos)}')
    for k, v in contatos.items():
        print(f'    * ID [{k}] - Nome: {v[0]}')
    input('''    ------------------------------------
    |  Pressione qualquer tecla para retornar ao menu principal...''')


def executar_funcao(funcao):
    if funcao == 1:
        adicionar_novo()
    elif funcao == 2:
        excluir_contato()
    elif funcao == 3:
        excluir_todos()
    elif funcao == 4:
        buscar_contato()
    elif funcao == 5:
        listar_contatos()
    elif funcao == 6:
        print('    | Agenda encerrada...')
    else:
        print('    >>> Função não implementada! <<<')


contatos = {}
funcao_selecionada = menu_principal()
executar_funcao(funcao_selecionada)
while funcao_selecionada != 6:
    funcao_selecionada = menu_principal()
    executar_funcao(funcao_selecionada)
