from time import sleep
from funcoes import cabecalho, menu

# Cadastro de valores - Receitas e Gastos

def cadastrar_valores(nome_sessao, lista, carregando, descricao):
    valor = float(input(f'Digite o valor que deseja inserir na sessão de {nome_sessao}: R$'))
    lista.append(valor)
    print('=' * 52)
    print(f'⚙️{carregando}...'.center(52))
    print('=' * 52)
    sleep(1)
    print()
    print(f'{descricao} com sucesso!✅')
    print()
    print(f'Valor: R${valor:.2f}')
    print()
    print('=' * 52)

# Cálculo do saldo + cálculo do total de receitas e gastos

def calculo_financeiro(receitas, gastos):
    total_receitas = sum(receitas)
    total_gastos = sum(gastos)
    saldo = total_receitas - total_gastos
    return total_receitas, total_gastos, saldo

# Interface do histórico

def mostrar_lista_valores(titulo, lista, simbolo):
    print()
    print(titulo)
    print()
    if not lista:
       print('Nenhum registro encontrado.')
       print()
    else:
        for valor in lista:
            print(f'{simbolo} R${valor:.2f}')
    print()
    print('-' * 40)
    print()

# Função de execução do controle financeiro

def executar_financeiro(receitas,gastos):
    while True:
        op2 = menu(
            '💵CONTROLE FINANCEIRO💵',
            'o seu espaço com seu dinheirinho',
            [
                '[1] Cadastrar Receita',
                '[2] Cadastrar Gasto',
                '[3] Calcular Saldo',
                '[4] Mostrar Histórico',
                '[5] Voltar',
            ],
            ['1', '2', '3', '4', '5'],
        )

        # Cadastro de Receita

        if op2 == '1':
            cadastrar_valores('Receita', receitas, 'DEPOSITANDO', 'Receita cadastrada')

        # Cadastro de Gastos

        elif op2 == '2':
            cadastrar_valores('Gastos', gastos, 'REGISTRANDO GASTOS', 'Registrado')

        # Cálculo de Saldo

        elif op2 == '3':
            total_receitas, total_gastos, saldo = calculo_financeiro(receitas, gastos)
            cabecalho('💰SALDO ATUAL💰', 'resumo das suas finanças')
            print()
            print(f'Total de receitas: R${total_receitas:.2f}')
            print()
            print(f'Total de gastos: R${total_gastos:.2f}')
            print()
            print(f'Saldo atual: R${saldo:.2f}')
            print()
            print('=' * 40)
            input('Pressione ENTER para voltar ao menu...')

        # Histórico Financeiro - Total de Receitas, Gastos e Saldo Atual

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