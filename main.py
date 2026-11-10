from funcoes import *
from financeiro import executar_financeiro
from wishlist import executar_wishlist
from skincare import executar_skincare
from metas import executar_metas

# Listas para Armazenar Dados - Controle Financeiro

receitas = []
gastos = []

# Lista para Armazenar Dados - WishList

wishlist = []

# Lista para Armazenar Dados - SkinCare

produtos_skincare = []

# Lista para Armazenar Dados - Metas

metas = []

# Menu Principal

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
        executar_metas(metas)

# Fim do Programa

    elif op == '5':
        print()
        print('Obrigada por desfrutar do LifeHub💖'.center(40))
        print('volte sempre!'.center(35))
        print()
        print('=' * 40)
        break
