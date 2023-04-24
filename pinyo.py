import os
from Biblioteca import Livro


# Constantes para as cores utilizadas
COR_ROXO = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;150;0;150m'
COR_BRANCO_NEGRITO = '\u001b[1m\u001b[38;2;255;255;255m'
COR_BRANCO_SUB = '\u001b[1m\u001b[38;2;255;255;255m\u001b[37;4;25;255;255m'
COR_AZUL = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;50;0;255m'


def formatar_texto_centralizado(texto: str, cor: str, tamanho_total: int) -> str:
    """Formata o texto para que fique centralizado no terminal."""
    tamanho_texto = len(texto)
    espacos = ' ' * ((tamanho_total - tamanho_texto) // 2)
    return f'{espacos}{cor}{texto}\u001b[m'


def imprimir_cabecalho_opcao(texto: str, cor: str, tamanho_total: int) -> None:
    """Imprime o cabeçalho para cada opção do menu."""
    print(f'{formatar_texto_centralizado("-"*len(texto), cor, tamanho_total)}')
    print(f'{formatar_texto_centralizado(texto, cor, tamanho_total)}')
    print(f'{formatar_texto_centralizado("-"*len(texto), cor, tamanho_total)}')


# Calculando o espaçamento necessário para centralizar o design
term_size = os.get_terminal_size()
central_space = ' ' * ((term_size.columns - 43) // 2)

# Imprimindo o design centralizado
print(formatar_texto_centralizado("Seja muito bem vindo a nossa biblioteca em python", COR_ROXO, term_size.columns))

while True:
    print('\n')
    imprimir_cabecalho_opcao("MENU DA BIBLIOTECA", COR_AZUL, term_size.columns)
    print(f'{formatar_texto_centralizado("Selecione a operação que você deseja executar:", COR_ROXO, term_size.columns)}')
    print(f'{formatar_texto_centralizado("1 - Ver os livros disponíveis", COR_BRANCO_SUB, term_size.columns)}')
    print(f'{formatar_texto_centralizado("2 - Ir para o menu de empréstimos", COR_BRANCO_SUB, term_size.columns)}')
    print(f'{formatar_texto_centralizado("3 - Ver seus livros emprestados", COR_BRANCO_SUB, term_size.columns)}')
    print(f'{formatar_texto_centralizado("4 - Devolver algum livro", COR_BRANCO_SUB, term_size.columns)}')
    print(f'{formatar_texto_centralizado("0 - Sair do programa.", COR_BRANCO_SUB, term_size.columns)}')
    selecione = input(f'{formatar_texto_centralizado("Digite o número da operação desejada: ", COR_BRANCO_NEGRITO, term_size.columns)}') 
    if selecione == '1':
        print('\n')
        imprimir_cabecalho_opcao("LIVROS DISPONÍVEIS", COR_AZUL, term_size.columns)
        Livro.deseja_listar()

    elif selecione == '2':
        print('\n')
        imprimir_cabecalho_opcao("MENU DE EMPRÉSTIMOS", COR_AZUL, term_size.columns)
        Livro.deseja_emprestar()

    elif selecione == '3':
        print('\n')
        imprimir_cabecalho_opcao("SEUS LIVROS EMPRESTADOS", COR_AZUL, term_size.columns)
        Livro.listar_livros_emprestados()
        input(f'\n{COR_BRANCO_SUB}Digite qualquer tecla para continuar: ')

    elif selecione == '4':
        print('\n')
        imprimir_cabecalho_opcao("DEVOLVER LIVRO", COR_AZUL, term_size.columns)
        Livro.deseja_devolver()

    elif selecione == '0':
        print('\n')
        print(formatar_texto_centralizado("Obrigado por utilizar nossa biblioteca em Python!", COR_ROXO, term_size.columns))
        break

    else:
        print('\n')
        print(formatar_texto_centralizado("Opção inválida. Tente novamente.", COR_ROXO, term_size.columns))
