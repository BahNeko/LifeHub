from time import sleep
from funcoes import menu, cabecalho, verificar_lista_vazia, validar_item_escolhido

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
    for i, produto in enumerate(lista, start=1):
        print(f'{i}. {produto["nome"]} - {produto["status"]}')
    print()
    print('=' * 40)

# Função de Execução

def executar_skincare(produtos_skincare):
    while True:
        op4 = menu(
            '🧴SKINCARE🧴',
            'sua rotina de cuidados',
            [
                '[1] Adicionar Produto',
                '[2] Ver Produtos',
                '[3] Remover Produto',
                '[4] Marcar como Acabado',
                '[5] Voltar'
            ],
            ['1', '2', '3', '4', '5'],
        )

        # Registrando Produtos na Lista

        if op4 == '1':
            produto = {}

            print('=' * 40)
            print('''Para registrarmos um novo produto,
    responda o formulário abaixo: ''')
            print('=' * 60)
            sleep(1)

            produto['nome'] = input('Nome do Produto: ').strip()
            produto['categoria'] = input('Categoria do Produto: ').strip()
            produto['periodo'] = input('Período de Uso: ').strip()
            produto['status'] = 'Em Uso'
            produtos_skincare.append(produto)

            print('=' * 40)
            print('⚙️REGISTRANDO...'.center(40))
            print('=' * 40)
            sleep(1.5)
            print('Registrado com sucesso!✅')

        # Mostrando Itens da Lista de Skincare

        elif op4 == '2':
            cabecalho('🧴SKINCARE🧴', 'sua rotina de cuidados')
            print()

            if verificar_lista_vazia(produtos_skincare):
                continue

            mostrar_detalhes_skincare(produtos_skincare)

            print()
            print('=' * 40)
            input('Pressione ENTER para voltar...')

        # Removendo Itens da Lista de Skincare

        elif op4 == '3':
            cabecalho('🗑️REMOVER ITEM🗑️', 'produto finalizado')
            print()

            if verificar_lista_vazia(produtos_skincare):
                continue

            mostrar_itens_skincare(produtos_skincare)

            opc = int(input('Digite o número do produto que deseja remover: '))

            opc = validar_item_escolhido(opc, produtos_skincare, 'Digite novamente o número do produto: ')

            print('=' * 40)
            print(f'⚙️REMOVENDO...'.center(40))
            print('=' * 40)
            item_removido = produtos_skincare.pop(opc - 1)

            sleep(1.5)
            print(f'Produto {item_removido["nome"]} removido com sucesso! ✅')
            input('Pressione ENTER para voltar...')

        # Marcar Produto como Acabado/Finalizado

        elif op4 == '4':
            cabecalho('✅MARCAR COMO ACABADO✅', 'os produtinhos chegaram ao fim')
            print()

            if verificar_lista_vazia(produtos_skincare):
                continue

            mostrar_itens_skincare(produtos_skincare)
            opc2 = int(input('Escolha a sua opção: '))

            opc2 = validar_item_escolhido(opc2, produtos_skincare, 'Digite novamente o número do produto: ')

            if produtos_skincare[opc2 - 1]['status'] == 'Acabado':
                print('Esse item já está marcado como acabado!')
                input('Pressione ENTER para voltar...')

            else:
                print('=' * 40)
                print(f'⚙️ALTERANDO STATUS...'.center(40))
                print('=' * 40)

                produtos_skincare[opc2 - 1]['status'] = 'Acabado'
                sleep(1.5)

                print(f'Produto {produtos_skincare[opc2 - 1]["nome"]} marcado como acabado! ✅')
                input('Pressione ENTER para voltar...')

        elif op4 == '5':
            break