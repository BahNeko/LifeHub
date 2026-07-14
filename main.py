from time import sleep

# Criando o Menu de Interações

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

# Validando se a opção tá dentro do menu de interações

    if op not in ['1', '2', '3', '4', '5', '6']:
        print('''Opção Inválida!
Pressione ENTER para continuar...''')
        input()

# Iniciando as telas selecionadas no menu de interações

    if op == '1':
        print('⚙️CARREGANDO...'.center(40))
        print('=' * 40)
        sleep(1.5)
        print('Controle Financeiro em desenvolvimento ⏳')
        print('pressione ENTER para voltar ao menu...')
        print('=' * 40)
        input()

    elif op == '2':
        print('⚙️CARREGANDO...'.center(40))
        print('=' * 40)
        sleep(1.5)
        print('WishList em desenvolvimento ⏳')
        print('pressione ENTER para voltar ao menu...')
        print('=' * 40)
        input()

    elif op == '3':
        print('⚙️CARREGANDO...'.center(40))
        print('='*40)
        sleep(1.5)
        print('Skincare em desenvolvimento ⏳')
        print('pressione ENTER para voltar ao menu...')
        print('='*40)
        input()

    elif op == '4':
        print('⚙️CARREGANDO...'.center(40))
        print('=' * 40)
        sleep(1.5)
        print('Receitas de Comida em desenvolvimento ⏳')
        print('pressione ENTER para voltar ao menu...')
        print('=' * 40)
        input()

    elif op == '5':
        print('⚙️CARREGANDO...'.center(40))
        print('=' * 40)
        sleep(1.5)
        print('Metas em desenvolvimento ⏳')
        print('pressione ENTER para voltar ao menu...')
        print('=' * 40)
        input()

    elif op == '6':
        print()
        print('Obrigada por desfrutar do LifeHub💖'.center(40))
        print('volte sempre!'.center(35))
        print()
        print('=' * 40)
        break