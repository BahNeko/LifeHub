from time import sleep

# Funções do Código - Cabeçalho dos Menus (ex: controle financeiro, wishlist etc)

def cabecalho(nome, descricao):
    print('=' * 40)
    print(nome.center(40))
    print(descricao.center(40))
    print('=' * 40)

# Interface de carregamento

def carregar_tela(nome):
    print('⚙️CARREGANDO...'.center(40))
    print('=' * 40)
    sleep(1.5)
    print(f'{nome} em desenvolvimento ⏳')
    print('pressione ENTER para voltar ao menu...')
    print('=' * 40)
    input()

# Validação das opções propostas no código

def validacao_opcao(opcao_digitada, opcoes_validas):
    while opcao_digitada not in opcoes_validas:
        print('Opção Inválida!')
        opcao_digitada = input('Tente digitar novamente: ').strip()
    return opcao_digitada

# Validação de Lista Vazia

def verificar_lista_vazia(lista):
    if not lista:
        print('Nenhum item cadastrado.')
        print()
        print('=' * 40)
        print()
        input('Pressione ENTER para voltar...')
        return True

    return False

# Validando o Item Escolhido

def validar_item_escolhido(opc, lista, mensagem):
    while opc < 1 or opc > len(lista):
        print('Opção Inválida! Tente novamente...')
        opc = int(input(mensagem))
    return opc

# Menus do Código

def menu(titulo, descricao, opcoes, opcoes_validas):
        cabecalho(titulo, descricao)
        print()

        for opcao in opcoes:
            print(opcao)
        print()
        print('=' * 40)

        op3 = str(input('Escolha uma opção: ')).strip()
        return validacao_opcao(op3, opcoes_validas)

# Listando as Metas

def mostrar_metas_detalhadas(lista):
    for m, meta in enumerate(lista, start=1):
        print(f'{m}. {meta["nome"]}')
        print(f'Categoria: {meta["categoria"]}')
        print(f'Prazo: {meta["prazo"]}')
        print(f'Progresso: {meta["progresso"]}%')
        print(f'Status: {meta["status"]}')
        print()
        print('-' * 40)
        print()

def mostrar_metas(lista):
    for m, meta in enumerate(lista, start=1):
        print(f'{m}. {meta["nome"]} - {meta["status"]} {meta["progresso"]}%')
    print()
    print('=' * 40)