from Biblioteca import Livro

cor1 = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;150;0;150m'
cor2 = '\u001b[1m\u001b[38;2;255;255;255m\u001b[37;4;25;255;255m'
cor3 = '\u001b[1m\u001b[38;2;255;255;255m'
cor4 = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;50;0;255m'

central_space = ' ' * 25

print(f'{central_space}{cor1}-------------Seja muito bem vindo a nossa biblioteca em python-------------\u001b[m')

while True:
    selecione = input(f'\n{central_space}    {cor4}MENU DA BIBLIOTECA\u001b[m\n\n{central_space}{cor1}Selecione a operação que você deseja executar:\u001b[m\n\n{central_space}{cor2}1 - Ver os livros disponíveis\u001b[m\n{central_space}{cor2}2 - Ir para o menu de empréstimos\u001b[m\n{central_space}{cor2}3 - Ver seus livros emprestados\u001b[m\n{central_space}{cor2}4 - Devolver algum livro\u001b[m\n{central_space}{cor2}0 - Sair do programa.\u001b[m\n{central_space}{cor3}Digite aqui: ')

    if selecione == '1':
        Livro.deseja_listar()

    elif selecione == '2':
        Livro.deseja_emprestar()

    elif selecione == '3':
        Livro.listar_livros_emprestados()
        input(f'\n{cor3}Digite qualquer tecla para continuar: ')

    elif selecione == '4':
        Livro.deseja_devolver()

    elif selecione == '0':
        print(f'\n{central_space}Muito obrigado por usar o nosso programa.\n')
        break

    else:
        print(f'{central_space}Valor inválido. Digite novamente!') 