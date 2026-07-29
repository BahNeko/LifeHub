from time import sleep

# Funções do Código - Cabeçalho dos Menus (ex: controle financeiro, wishlist etc)

def cabecalho(nome, descricao):
    print('=' * 40)
    print(nome.center(40))
    print(descricao.center(40))
    print('=' * 40)

# "Gracinha KKKKK" de carregamento

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

# Cadastro de valores no Controle Financeiro - Receitas e Gastos

def cadastrar_valores(nome_sessao, lista, carregando, descricao):
    valor = float(input(f'Digite o valor que deseja inserir na sessão de {nome_sessao}: R$'))
    lista.append(valor)
    print('=' * 52)
    print(f'⚙️{carregando}...'.center(52))
    print('=' * 52)
    sleep(1)
    print()
    print(f'{descricao} com sucesso!✅')
    print()
    print(f'Valor: R${valor:.2f}')
    print()
    print('=' * 52)

# Cálculo do saldo + cálculo do total de receitas e gastos

def calculo_financeiro(receitas, gastos):
    total_receitas = sum(receitas)
    total_gastos = sum(gastos)
    saldo = total_receitas - total_gastos
    return total_receitas, total_gastos, saldo

# Interface do histórico de controle financeiro

def mostrar_lista_valores(titulo, lista, simbolo):
    print()
    print(titulo)
    print()
    if not lista:
       print('Nenhum registro encontrado.')
       print()
    else:
        for valor in lista:
            print(f'{simbolo} R${valor:.2f}')
    print()
    print('-' * 40)
    print()

# Validação de Lista Vazia - Wishlist

def verificar_lista_vazia(lista):
    if not lista:
        print('Nenhum item cadastrado.')
        print()
        print('=' * 40)
        print()
        input('Pressione ENTER para voltar...')
        return True

    return False

# Listando a WishList

def mostrar_itens_wishlist(lista):
    for i, item, in enumerate(lista, start=1):
        print(f'{i}. {item["nome"]} - {item["status"]}')
    print()
    print('=' * 40)

# Listando a WishList de Forma Detalhada

def mostrar_detalhes_wishlist(lista):
    for i, item in enumerate(lista, start=1):
        print(f'{i}. {item["nome"]}')
        print(f'Categoria: {item["categoria"]}')
        print(f'Preço: R$ {item["preco"]:.2f}')
        print(f'Status: {item["status"]}')
        print()
        print('-' * 40)
        print()

# Validando a Opção na WishList

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

# Listando a Skincare

def mostrar_detalhes_skincare(lista):
    for i, produto in enumerate(lista, start=1):
        print(f'{i}. {produto["nome"]}')
        print(f'Categoria: {produto["categoria"]}')
        print(f'Período: {produto["periodo"]}')
        print(f'Status: {produto["status"]}')
        print()
        print('-' * 40)
        print()

# Mostrando Itens da Lista Skincare

def mostrar_itens_skincare(lista):
    for i, produto, in enumerate(lista, start=1):
        print(f'{i}. {produto["nome"]} - {produto["status"]}')
    print()
    print('=' * 40)