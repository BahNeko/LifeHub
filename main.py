from funcoes import *

# Listas para Armazenar Dados - Controle Financeiro

receitas = []
gastos = []

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
               cadastrar_valores('Receita', receitas, 'DEPOSITANDO', 'Receita cadastrada')

# Cadastro de Gastos

            elif op2 == '2':
                cadastrar_valores('Gastos', gastos, 'REGISTRANDO GASTOS', 'Registrado')

# Cálculo de Saldo

            elif op2 == '3':
                total_receitas, total_gastos, saldo = calculo_financeiro(receitas, gastos)
                cabecalho('💰SALDO ATUAL💰', 'resumo das suas finanças' )
                print()
                print(f'Total de receitas: R${total_receitas:.2f}')
                print()
                print(f'Total de gastos: R${total_gastos:.2f}')
                print()
                print(f'Saldo atual: R${saldo:.2f}')
                print()
                print('=' * 40)
                input('Pressione ENTER para voltar ao menu...')

            elif op2 == '4':
                total_receitas, total_gastos, saldo = calculo_financeiro(receitas, gastos)
                cabecalho('📜HISTÓRICO FINANCEIRO📜', 'todas as suas movimentações')
                mostrar_lista_valores('💵RECEITAS', receitas, '+')
                mostrar_lista_valores('💸GASTOS', gastos, '-')
                print('📊RESUMO')
                print()
                print(f'Total de receitas: R${total_receitas:.2f}')
                print(f'Total de gastos: R${total_gastos:.2f}')
                print()
                print(f'Saldo atual: R${saldo:.2f}')
                print()
                print('=' * 40)
                input('Pressione ENTER para voltar ao menu...')

            elif op2 == '5':
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
