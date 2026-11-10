from time import sleep
from funcoes import menu, cabecalho, validar_item_escolhido, verificar_lista_vazia

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
        input('Pressione ENTER para continuar...')
        print()

# Progresso das Metas

def mostrar_metas(lista):
    for m, meta in enumerate(lista, start=1):
        print(f'{m}. {meta["nome"]} - {meta["status"]} {meta["progresso"]}%')
    print()
    print('=' * 40)

# Função de Execução

def executar_metas(metas):
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

        elif op5 == '4':
            cabecalho('🗑️REMOVER META🗑️', 'gerencie suas metas')
            print()

            if verificar_lista_vazia(metas):
                continue

            mostrar_metas(metas)
            opc4 = int(input('Escolha o número da meta que deseja remover: '))

            opc4 = validar_item_escolhido(opc4, metas, 'Digite novamente a meta escolhida: ')

            print('=' * 40)
            print(f'⚙️REMOVENDO...'.center(40))
            print('=' * 40)
            item_removido = metas.pop(opc4 - 1)

            sleep(1.5)
            print(f'Meta "{item_removido["nome"]}" removida com sucesso! ✅')
            input('Pressione ENTER para voltar...')

        elif op5 == '5':
            break