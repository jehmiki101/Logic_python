# REFATORAÇÃO PRINTS
def invalido():
    print('Opção Inválida')

# C - Função cadastrar livros
def cadastrar_livro(id):
    # Menu de cadastrar livro
    print('-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', '-' * 14)
    # C.a - inputs de nome, autor e editora do livro a ser cadastrado
    while True:
        nome = input('Qual o nome do livro? ')
        if (nome == ''):
            invalido()
            continue
        else:
            while True:
                autor = input('Qual o autor do livro? ')
                if (autor == ''):
                    invalido()
                    continue
                else:
                    while True:
                        editora = input('Qual a editora do livro? ')
                        if (editora == ''):
                            invalido()
                            continue
                        else:
                            # C.b - Armazenamento do id, nome, autor e editora em dicionário
                            dic_lista = {'id':id,'nome':nome,'autor':autor,'editora':editora}
                            # C.c - Copiar dicionário para a lista_livro
                            global lista_livro
                            lista_livro.append(dic_lista)
                            print('Cadastro feito com sucesso!')
                        break
                break
        break

# D - Função de consulta de livro
def consultar_livro():
    while True:
        menu_consultar()
        consulta = int(input('>>'))
        # D.a.V - Opção inválida de input
        if (consulta != 1 and consulta != 2 and consulta != 3 and consulta != 4):
            invalido()
            continue
        # D.a.VI - Retornar ao menu principal
        elif (consulta == 4):
            print('Voltando ao menu principal')
            break
        # D.a.I - Consultar todos os livros cadastrados
        elif (consulta == 1):
            consulta_geral()
            continue
        # D.a.II - Consultar livro por Id
        elif (consulta == 2):
            consulta_id()
            continue
        # D.a.III - Consultar livro por Autor
        else:
            consulta_autor()
            continue

# D.a - Menu consultar livro
def menu_consultar():
    print('-' * 50)
    print('-' * 14, 'MENU CONSULTAR LIVRO', '-' * 14)
    print('Escolha a opção desejada: ')
    print('1 - Consultar Todos')
    print('2 - Consultar por Id')
    print('3 - Consultar por Autor')
    print('4 - Retornar ao menu')

# D.a.I - função consultar todos os livros cadastrados
def consulta_geral():
    print('-' * 30)
    global lista_livro
    for dic in lista_livro:
        print('id: ', dic['id'])
        print('nome: ', dic['nome'])
        print('autor: ', dic['autor'])
        print('editora: ', dic['editora'])
        print(' ')

# D.a.II - Consultar livro por Id
def consulta_id():
    print('-' * 30)
    global lista_livro
    while True:
        inp_id = int(input('Digite o id do livro: '))
        if (inp_id <= 0):
            invalido()
            continue
        for dic in lista_livro:
            if (inp_id == dic['id']):
                print('id: ', dic['id'])
                print('nome: ', dic['nome'])
                print('autor: ', dic['autor'])
                print('editora: ', dic['editora'])
        break

# D.a.III - Consultar livro por Autor
def consulta_autor():
    print('-' * 30)
    global lista_livro
    while True:
        try:
            inp_autor = input('Digite o Autor do livro: ')
            for dic in lista_livro:
                if (dic.get('autor') == inp_autor):
                    print('id: ', dic['id'])
                    print('nome: ', dic['nome'])
                    print('autor: ', dic['autor'])
                    print('editora: ', dic['editora'])
                    print(' ')
                    continue
                else:
                    invalido()
        except:
            invalido()
        break

# E - Função de remover livros
def remover_livro():
    while True:
        try:
            # E.a - Pergunta o livro a ser removido
            inp_remove = int(input('Digite o id do livro a ser removido: '))
            if (inp_remove <= len(lista_livro) and inp_remove > 0):
                index = 0
                # E.b - Remoção de livro da lista
                for i in range(len(lista_livro)):
                    if (lista_livro[i].get('id') == inp_remove):
                        index = i
                lista_livro.pop(index)
                print('Livro removido com sucesso!')
                break
            # E.c - Id fornecido não está na lista
            else:
                print('Id Inválido')
                break
        # Id inválido para outros inputs
        except:
            invalido()

# CÓDIGO PRINCIPAL / MAIN
# A - Print com mensagem de boas vidas e nome
print('Bem vindo a Livraria da Jéssica Hara!')
# B - lista vazia lista_livro e variável id_global
lista_livro = []
id_global = 0

# Escolha de serviço
while True:
    # F.a - estrutura do menu principal
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Encerrar programa')
    try:
        servico = int(input('>> '))# input escolha do servico
        if (servico != 1 and servico != 2 and servico != 3 and servico != 4):# F.a.V e VI - opção inválida e continuação do menu
            invalido()
            continue
        elif (servico == 4):# F.a.IV - encerrar programa
            print('Saindo do sistema')
            break
        elif (servico == 1):# F.a.I - cadastro de livro
            id_global += 1
            cadastrar_livro(id_global)
            continue
        elif (servico == 2):# F.a.II - consulta de livro
            consultar_livro()
            #D.a.IV - voltar ao menu principal
            continue
        elif (servico == 3):# F.a.III - remover livro
            remover_livro()
            continue
    # F.a.VI - Opção inválida para oureos inputs
    except:
        invalido()