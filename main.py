from time import sleep

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

# Validando se a opção está dentro do menu de interações

    if op not in ['1', '2', '3', '4', '5', '6']:
        print('''Opção Inválida!
Pressione ENTER para continuar...''')
        input()
        continue

# Iniciando as telas selecionadas no menu de interações

    if op == '1':
        cabecalho('💵CONTROLE FINANCEIRO💵', 'o seu espaço com seu dinheirinho')


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