from funcoes import cabecalho, menu, verificar_lista_vazia, validar_item_escolhido
from time import sleep

# Listando a WishList

def mostrar_itens_wishlist(lista):
    for i, item in enumerate(lista, start=1):
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

# Função de Execução da WishList

def executar_wishlist(wishlist):
    while True:
        op3 = menu(
            '🎁WISHLIST🎁',
            'seus desejos e objetivos',
            [
                '[1] Adicionar item',
                '[2] Ver Wishlist',
                '[3] Remover item',
                '[4] Marcar como comprado',
                '[5] Voltar'
            ],
            ['1', '2', '3', '4', '5']
        )

        # Registrando um Item na WishList

        if op3 == '1':
            item = {}

            print('=' * 40)
            print('''Para seguirmos com o registro do novo item,
    preciso que responda esse pequeno formulário a seguir''')
            print('=' * 60)
            sleep(1)

            item['nome'] = str(input('Nome do Item: ')).strip()
            item['categoria'] = str(input('Categoria do Item: ')).strip()
            item['preco'] = float(input('Preço do Item (apenas números, por gentileza): R$'))
            item['status'] = 'Pendente'
            wishlist.append(item)

            print('=' * 40)
            print('⚙️REGISTRANDO...'.center(40))
            print('=' * 40)
            sleep(1.5)
            print('Registrado com sucesso!✅')

        # Mostrar a WishList na Tela

        elif op3 == '2':
            cabecalho('🎁WISHLIST🎁', 'seus desejos e objetivos')
            print()

            if verificar_lista_vazia(wishlist):
                continue

            mostrar_detalhes_wishlist(wishlist)

            print()
            print('=' * 40)
            input('Pressione ENTER para voltar...')

        # Removendo Itens da WishList

        elif op3 == '3':
            cabecalho('🗑️REMOVER ITEM🗑️', 'metas alcançadas')
            print()

            if verificar_lista_vazia(wishlist):
                continue

            mostrar_itens_wishlist(wishlist)

            opc = int(input('Digite o número do item que deseja remover: '))

            opc = validar_item_escolhido(opc, wishlist, 'Digite novamente a sua opção: ')

            print('=' * 40)
            print(f'⚙️REMOVENDO...'.center(40))
            print('=' * 40)
            item_removido = wishlist.pop(opc - 1)

            sleep(1.5)
            print(f'Item "{item_removido["nome"]}" removido com sucesso! ✅')
            input('Pressione ENTER para voltar...')

        # Marcar Como Comprado/Check na WishList

        elif op3 == '4':
            cabecalho('✅MARCAR COMO COMPRADO✅', 'comprinhas realizadas')
            print()

            if verificar_lista_vazia(wishlist):
                continue

            mostrar_itens_wishlist(wishlist)
            opc2 = int(input('Escolha sua opção: '))

            opc2 = validar_item_escolhido(opc2, wishlist, 'Digite novamente a sua opção: ')

            if wishlist[opc2 - 1]['status'] == 'Comprado':
                print('Esse item já está marcado como comprado!')
                input('Pressione ENTER para voltar...')

            else:
                print('=' * 40)
                print(f'⚙️ALTERANDO STATUS...'.center(40))
                print('=' * 40)

                wishlist[opc2 - 1]['status'] = 'Comprado'
                sleep(1.5)

                print(f'Item {wishlist[opc2 - 1]["nome"]} marcado como comprado! ✅')
                input('Pressione ENTER para voltar...')

        elif op3 == '5':
            break