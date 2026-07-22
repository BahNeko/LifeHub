from funcoes import *

# Listas para Armazenar Dados - Controle Financeiro

receitas = []
gastos = []

# Lista e para Armazenar Dados - WishList

wishlist = []

# Código Principal - Criando o Menu de Interações

while True:
    cabecalho('⭐LIFEHUB⭐', 'o seu sistema de organização pessoal')
    print()
    print('''[1] Controle Financeiro
[2] WishList
[3] Skincare
[4] Metas
[5] Sair''')
    print()
    print('='*40)

    op = str(input('Escolha uma opção: ')).strip()
    print('='*40)

    op = validacao_opcao(op, ['1', '2', '3', '4', '5',])

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
        while True:
            cabecalho('🎁WISHLIST🎁', 'seus desejos e objetivos')
            print()
            print('''[1] Adicionar item
[2] Ver Wishlist
[3] Remover item
[4] Marcar como comprado
[5] Voltar''')
            print()
            print('=' * 40)

            op3 = str(input('Escolha uma opção ')).strip()

            op3 = validacao_opcao(op3, ['1', '2', '3', '4', '5'])

            if op3 == '1':
                item = {}

                print('='*40)
                print('''Para seguirmos com o registro do novo item,
preciso que responda esse pequeno formulário a seguir''')
                print('='*60)
                sleep(1)

                item['nome']=str(input('Nome do Item: ')).strip()
                item['categoria']=str(input('Categoria do Item: ')).strip()
                item['preco']=float(input('Preço do Item (apenas números, por gentileza): R$'))
                item['status']= 'Pendente'
                wishlist.append(item)

                print('='*40)
                print('⚙️REGISTRANDO...'.center(40))
                print('=' * 40)
                sleep(1.5)
                print('Registrado com sucesso!✅')

            elif op3 == '2':
                cabecalho('🎁WISHLIST🎁', 'seus desejos e objetivos')
                print()

                if not wishlist:
                    print('Nenhum item cadastrado.')

                else:
                    for i, item in enumerate(wishlist, start=1):
                        print(f'{i}.')
                        print(f'Nome: {item["nome"]}')
                        print(f'Categoria: {item["categoria"]}')
                        print(f'Preço: R$ {item["preco"]:.2f}')
                        print(f'Status: {item["status"]}')
                        print()
                        print('-'*40)
                        print()

                print()
                print('=' * 40)
                input('Pressione ENTER para voltar...')

            elif op3 == '3':
                cabecalho('🗑️REMOVER ITEM🗑️', 'metas alcançadas')
                print()

                if not wishlist:
                    print('Nenhum item cadastrado.')
                    print()
                    print('='*40)
                    input('Pressione ENTER para voltar...')

                else:
                    for i, item in enumerate(wishlist, start=1):
                        print(f'{i}. {item["nome"]}')

                    print()
                    print('-'*40)
                    opc = int(input('Digite o número do item que deseja remover: '))

                    while opc < 1 or opc > len(wishlist):
                        print('Opção Inválida! Tente novamente...')
                        opc = int(input('Digite o número do item que deseja remover: '))

                    print('='*40)
                    print(f'⚙️REMOVENDO...'.center(40))
                    print('='*40)
                    item_removido = wishlist.pop(opc - 1)

                    sleep(1.5)
                    print(f'Item "{item_removido["nome"]}" removido com sucesso! ✅')
                    input('Pressione ENTER para voltar...')


            elif op3 == '5':
                break

    elif op == '3':
        carregar_tela('Skincare')

    elif op == '4':
        carregar_tela('Metas')

    elif op == '5':
        print()
        print('Obrigada por desfrutar do LifeHub💖'.center(40))
        print('volte sempre!'.center(35))
        print()
        print('=' * 40)
        break
