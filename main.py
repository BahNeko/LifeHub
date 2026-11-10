from funcoes import *
from financeiro import executar_financeiro
from wishlist import executar_wishlist
from skincare import executar_skincare

# Listas para Armazenar Dados - Controle Financeiro

receitas = []
gastos = []

# Lista para Armazenar Dados - WishList

wishlist = []

# Lista para Armazenar Dados - SkinCare

produtos_skincare = []

# Lista para Armazenar Dados - Metas

metas = []

# Código Principal - Criando o Menu de Interações

while True:
    op = menu(
        '⭐LIFEHUB⭐',
        'o seu sistema de organização pessoal',
        [
    '[1] Controle Financeiro',
    '[2] WishList',
    '[3] Skincare',
    '[4] Metas',
    '[5] Sair'
    ],
    ['1', '2', '3', '4', '5']
    )

# Controle Financeiro

    if op == '1':
        executar_financeiro(receitas, gastos)

# WishList

    elif op == '2':
        executar_wishlist(wishlist)

# Skincare

    elif op == '3':
        executar_skincare(produtos_skincare)

# Metas

    elif op == '4':
        while True:
            op5 = menu(
                '🎯METAS🎯',
                'um passo de cada vez',
                [
                    '[1] Adicionar Meta',
                    '[2] Ver Metas',
                    '[3] Atualizar Progresso',
                    '[4] Remover Meta',
                    '[5] Voltar'
                ],
                ['1', '2', '3', '4', '5'])

# Registrando Metas

            if op5 == '1':
                meta = {}

                print('=' * 40)
                print('''Para registrarmos uma nova meta,
responda o formulário abaixo...''')
                print('=' * 60)
                sleep(1)

                meta['nome'] = input('Meta: ').strip()
                meta['categoria'] = input('Categoria: ').strip()
                meta['prazo'] = input('Prazo: ').strip()
                meta['progresso'] = 0
                meta['status'] = 'Em Andamento'
                metas.append(meta)

                print('=' * 40)
                print('⚙️REGISTRANDO...'.center(40))
                print('=' * 40)
                sleep(1.5)
                print('Registrada com sucesso!✅')

# Mostrando a Lista de Metas

            elif op5 == '2':
                cabecalho('🎯METAS🎯', 'suas metas em um só lugar')
                print()

                if verificar_lista_vazia(metas):
                    continue

                mostrar_metas_detalhadas(metas)

# Atualizando Progresso da Meta

            elif op5 == '3':
                cabecalho('⚙️ATUALIZAR PROGRESSO⚙️', 'suas metas indo pra frente')
                print()

                if verificar_lista_vazia(metas):
                    continue

                mostrar_metas(metas)
                opc3 = int(input('Escolha a sua opção: '))

                opc3 = validar_item_escolhido(opc3, metas, 'Digite novamente a meta escolhida: ')

                sleep(0.5)
                porcentagem_progresso = int(input('Qual a % do seu progresso atualmente?: '))

                while porcentagem_progresso < 0 or porcentagem_progresso > 100:
                    print('O progresso deve estar entre 0% e 100%')
                    porcentagem_progresso = int(input('Qual a % do seu progresso atualmente?: '))

                metas[opc3 - 1]['progresso'] = porcentagem_progresso

                if metas[opc3 - 1]['progresso'] == 100:
                    metas[opc3 - 1]['status'] = 'Meta Concluída'
                else:
                    metas[opc3 - 1]['status'] = 'Em Andamento'

                print('=' * 40)
                print('⚙️ATUALIZANDO...'.center(40))
                print('=' * 40)
                sleep(1.5)

                print(f'Meta "{metas[opc3 - 1]["nome"]}" atualizada para {porcentagem_progresso}%!✅')
                print('=' * 40)

                input('Pressione ENTER para voltar...')

# Remover a Meta da Lista

            elif op5 == '5':
                break


    elif op == '5':
        print()
        print('Obrigada por desfrutar do LifeHub💖'.center(40))
        print('volte sempre!'.center(35))
        print()
        print('=' * 40)
        break
