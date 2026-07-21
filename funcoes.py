from time import sleep

# Funções do Código - Cabeçalho dos Menus (ex: controle financeiro, wishlist etc)

def cabecalho(nome, descricao):
    print('=' * 40)
    print(nome.center(40))
    print(descricao.center(40))
    print('=' * 40)

# "Gracinha KKKKK" de carregamento

def carregar_tela(nome):
    print('⚙️CARREGANDO...'.center(40))
    print('=' * 40)
    sleep(1.5)
    print(f'{nome} em desenvolvimento ⏳')
    print('pressione ENTER para voltar ao menu...')
    print('=' * 40)
    input()

# Validação das opções propostas no código

def validacao_opcao(opcao_digitada, opcoes_validas):
    while opcao_digitada not in opcoes_validas:
        print('Opção Inválida!')
        opcao_digitada = input('Tente digitar novamente: ').strip()
    return opcao_digitada

# Cadastro de valores no Controle Financeiro - Receitas e Gastos

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

# Interface do histórico de controle financeiro

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