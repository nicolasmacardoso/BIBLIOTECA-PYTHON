class ItemBiblioteca:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f"{self.__titulo} de {self.__autor} ({self.__ano_publicacao})"

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False

            print(f"\n{self.__titulo} emprestado com sucesso.")
            input('\nDigite qualquer tecla para continuar: ')

        else:
            print(f"\n{self.__titulo} não está disponível para empréstimo no momento.")
            input('\nDigite qualquer tecla para continuar: ')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True

            print(f"\n{self.__titulo} devolvido com sucesso.")
            input('\nDigite qualquer tecla para continuar: ')

        else:
            print(f"\n{self.__titulo} já está disponível para empréstimo.")
            input('\nDigite qualquer tecla para continuar: ')

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, num_paginas):
        super(). __init__(titulo, autor, ano_publicacao)

        self.__num_paginas = num_paginas

    def __str__(self):
        return f"{super().__str__()} - {self.__num_paginas} páginas"

    def listar_livros_disponiveis():  
        if len(lista_disponiveis) == 0 :
            print(f'\n{cor5}Não há livros disponíveis.')

        print(f'\n{cor1}------------Lista de livros disponíveis------------\u001b[m\n')

        for c in range(0,len(lista_disponiveis)) :
            print(f'{cor3}\u001b[48;2;{0 + 10*c};0;{0 + 25*c - 3*c}mLivro {c + 1}: {lista_disponiveis[c]}\u001b[m')

    def listar_livros_emprestados():
        if len(lista_emprestados) == 0 :
            print(f'\n{cor5}Você não possui nenhum livro.\u001b[m')

        print(f'\n{cor1}------------Livros na sua conta------------\u001b[m\n')

        for c in range(0,len(lista_emprestados)) :
            print(f'{cor3}\u001b[48;2;{115 - 12*c};0;{135 - 5*c}mLivro {c + 1}: {lista_emprestados[c]}\u001b[m')

    def deseja_listar():
        while True :
            s = input('\nDeseja exibir os livros disponíveis? [S/N]: ').upper()

            if s == 'S':
                Livro.listar_livros_disponiveis()
                input(f'\n{cor3}Digite qualquer tecla para continuar: ')

                break

            elif s == 'N':

                break

            else : 
                s = print('Valor inválido, digite "S" para SIM e "N" para NÃO. ')

                continue
            
    def deseja_emprestar():
            if len(lista_emprestados) == 10 :
                print(f'{cor5}\nVocê já possui todos os livros disponíveis.')
                input('\nDigite qualquer tecla para continuar: ')

            else :
                while True:
                    d = input(f'\n{espaço}{cor4} MENU DE EMPRÉSTIMOS DE LIVROS \u001b[m \n\n                {cor1} Selecione a operação que você deseja executar: \u001b[m\n\n{espaço}{cor2} 1 - Listar os livros disponíveis para empréstimo \u001b[m\n{espaço}{cor2} 2 - Listar os livros que você possui \u001b[m\n{espaço}{cor2} 3 - Pegar um livro emprestado\u001b[m\n{espaço}{cor2} 0 - Sair deste menu.\u001b[m\n{cor3}Digite aqui: ')

                    if d == '1' :
                        Livro.listar_livros_disponiveis()
                        input(f'{cor3}\nDigite qualquer tecla para continuar: ')

                    elif d == '2' :
                        Livro.listar_livros_emprestados()
                        input(f'{cor3}\nDigite qualquer tecla para continuar: ')

                    elif d == '3':
                        
                        if len(lista_disponiveis) == 0 :
                            print('Você já possui todos os livros disponíveis.')
                            input('\nDigite qualquer tecla para continuar: ')
                            break

                        else :                               
                            while True:
                                try:
                                    e = int(input('Selecione o livro desejado: ')) - 1

                                    break

                                except ValueError:
                                    print('Formato errado, digite um número.')

                            while True:
                                if e in range(len(lista_disponiveis)):
                                    Livro.emprestar(lista_disponiveis[e])
                                    lista_emprestados.append(lista_disponiveis[e])
                                    del lista_disponiveis[e]

                                    break

                                else : 
                                    try:
                                        if len(lista_disponiveis) == 1:
                                            e = int(input(f'Valor inválido, você possui apenas o livro 1: {lista_disponiveis[0]} Disponível para empréstimo. \nSelecione o livro desejado: ')) - 1
                                            
                                        else :
                                            e = int(input(f'Valor inválido, apenas livros de 1 a {len(lista_disponiveis)}. \nSelecione o livro desejado: ')) - 1

                                    except ValueError:
                                        print('Formato errado, digite um número.')

                                        continue

                    elif d == '0':

                        break

                    else :
                        print('Valor inválido, digite 1, 2, 3 ou 0.\n')

    def deseja_devolver():
            while True :

                if len(lista_emprestados) == 0 :
                    print(f'\n{cor5}Nenhum item disponível para devolução.\u001b[m')
                    input(f'\n{cor3}Digite qualquer tecla para continuar: ')

                    break

                s = input('Deseja devolver algum livro? [S/N]: ').upper()
                
                if s == 'S':
                    Livro.listar_livros_emprestados()

                    while True:
                        try:
                            d = int(input(f'{cor3}Selecione o livro desejado: ')) - 1

                            break

                        except ValueError:
                            print(f'{cor3}Formato errado, digite um número.\u001b[m')

                    while True:
                        if d in range(len(lista_emprestados)):
                            Livro.devolver(lista_emprestados[d])
                            lista_disponiveis.append(lista_emprestados[d])
                            del lista_emprestados[d]

                            break

                        else : 
                            try:
                                if len(lista_emprestados) == 1:
                                    d = int(input(f'{cor3}Valor inválido, você possui apenas o livro 1: {lista_emprestados[0]} Disponível para devolução. \nSelecione o livro desejado: ')) - 1
                                    
                                else :
                                    d = int(input(f'{cor3}Valor inválido, apenas livros de 1 a {len(lista_emprestados)}. \nSelecione o livro desejado: ')) - 1

                            except ValueError:
                                print('Formato errado, digite um número.')

                                continue
                            
                    if len(lista_emprestados) == 0 :

                        break

                    else :
                        o = input('Deseja devolver outro livro? [S/N]: ').upper()

                        if o == 'S':
                            Livro.listar_livros_emprestados()

                            while True:
                                try:
                                    d = int(input('Selecione o livro desejado: ')) - 1

                                    break

                                except ValueError:
                                    print('Formato errado, digite um número.')

                            while True:
                                if d in range(len(lista_emprestados)):
                                    Livro.devolver(lista_emprestados[d])
                                    lista_disponiveis.append(lista_emprestados[d])
                                    del lista_emprestados[d]

                                    break

                                else : 
                                    try:
                                        if len(lista_emprestados) == 1:
                                            d = int(input(f'Valor inválido, você possui apenas o livro 1: {lista_emprestados[0]} Disponível para devolução. Selecione o livro desejado: ')) - 1
                                    
                                        else :
                                            d = int(input(f'Valor inválido, apenas livros de 1 a {len(lista_emprestados)}. Selecione o livro desejado: ')) - 1

                                        break

                                    except ValueError:
                                        print('Formato errado, digite um número.')

                                        continue

                        elif o == 'N':

                            break

                        else:
                            print('Valor inválido, tente novamente!')

                            continue

                elif s == 'N':

                    break

                else :
                    print('Valor inválido, tente novamente!')

                    continue

livro1  = Livro("Dom Casmurro", "Machado de Assis", 1899, 256)
livro2  = Livro("O Poder do Hábito", "Charles Duhigg", 2012, 408)
livro3  = Livro("O Poder da Ação", "Paulo Vieira", 2015 , 256)
livro4  = Livro("Authenticgames", "Marco Túlio", 2016, 160)
livro5  = Livro("Como fazer amigos e influenciar pessoas", "Dale Carnegie", 2019, 256)
livro6  = Livro("O Príncipe", "Maquiavel", 2019, 130 )
livro7  = Livro("A arte da guerra", "Sun Tzu", 2019, 160)
livro8  = Livro("A revolução dos bichos", "George Orwell", 2007, 152)
livro9  = Livro("Felipe Neto: O influenciado", "Nelson Lima Neto", 2021, 267)
livro10 = Livro("De volta ao jogo: Uma Aventura Não Oficial De Minecraft", "RezendeEvil", 2016, 128)

lista_emprestados = []
lista_disponiveis = []

for c in range(1,10):
    lista_disponiveis.append(eval(f'livro{c}'))



espaço = '                        '
cor1 = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;150;0;150m'
cor2 = '\u001b[1m\u001b[38;2;255;255;255m\u001b[37;4;25;255;255m'
cor3 = '\u001b[1m\u001b[38;2;255;255;255m'
cor4 = '\u001b[1m\u001b[48;2;25;0;50m\u001b[38;2;255;255;255m'
cor5 = '\u001b[1m\u001b[48;2;0;0;0m\u001b[38;2;50;0;255m'
