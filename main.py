from time import sleep

# Listas e Dicionários para Armazenar Dados - Controle Financeiro

receitas = []
gastos = []

# Funções do Código

def cabecalho(nome, descricao):
    print('=' * 40)
    print(nome.center(40))
    print(descricao.center(40))
    print('=' * 40)

def carregar_tela(nome):
    print('⚙️CARREGANDO...'.center(40))
    print('=' * 40)
    sleep(1.5)
    print(f'{nome} em desenvolvimento ⏳')
    print('pressione ENTER para voltar ao menu...')
    print('=' * 40)
    input()

def validacao_opcao(opcao_digitada, opcoes_validas):
    while opcao_digitada not in opcoes_validas:
        print('Opção Inválida!')
        opcao_digitada = input('Tente digitar novamente: ').strip()
    return opcao_digitada


# Código Principal - Criando o Menu de Interações

while True:
    print('='*40)
    print('⭐LIFEHUB⭐'.center(35))
    print('o seu sistema de organização pessoal'.center(40))
    print('='*40)
    print()

    print('''[1] Controle Financeiro
[2] WishList
[3] Skincare
[4] Receitas de Comida
[5] Metas
[6] Sair''')
    print()
    print('='*40)

    op = str(input('Escolha uma opção: ')).strip()
    print('='*40)

    op = validacao_opcao(op, ['1', '2', '3', '4', '5', '6'])

# Menu - Controle Financeiro

    if op == '1':
        while True:
            cabecalho('💵CONTROLE FINANCEIRO💵', 'o seu espaço com seu dinheirinho')
            print()
            print('''[1] Cadastrar Receita
[2] Cadastrar Gasto
[3] Calcular Saldo
[4] Mostrar Histórico
[5] Voltar''')
            print()
            print('='*40)

            op2 = str(input('Escolha uma opção: ')).strip()
            print('='*52)

            op2 = validacao_opcao(op2, ['1', '2', '3', '4', '5'])

# Cadastro de Receita

            if op2 == '1':
                receita = float(input('Digite o valor que deseja inserir na receita: R$'))
                receitas.append(receita)
                print('='*52)
                print('⚙️DEPOSITANDO...'.center(52))
                sleep(1)
                print(f'Valor de {receita} depositado com sucesso!✅'.center(53))
                print('=' * 52)

            if op2 == '5':
                break

    elif op == '2':
        carregar_tela('Wishlist')

    elif op == '3':
        carregar_tela('Skincare')

    elif op == '4':
        carregar_tela('Receitas de Comida')

    elif op == '5':
        carregar_tela('Metas')

    elif op == '6':
        print()
        print('Obrigada por desfrutar do LifeHub💖'.center(40))
        print('volte sempre!'.center(35))
        print()
        print('=' * 40)
        break