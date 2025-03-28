# C - função cadastrar livros #OK
def cadastrar_livro(id):
    # Menu de cadastrar livro
    print('-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', '-' * 14)
    while True:
        # C.a - inputs de nome, autor e editora do livro a ser cadastrado
        nome = input('Qual o nome do livro? ')
        autor = input('Qual o autor do livro? ')
        editora = input('Qual a editora do livro? ')
        # C.b - Armazenamento do id, nome, autor e editora em dicionário
        dic_lista = {'id':id,'nome':nome,'autor':autor,'editora':editora}
        print(f'{dic_lista}') #ERASE
        # C.c - Copiar dicionário para a lista_livro
        global lista_livro
        lista_livro.append(dic_lista)
        break

# D - função de consulta de livro
def consultar_livro():
    while True:
        menu_consultar()
        consulta = int(input('>>'))
        # D.a.V - Opção inválida de input
        if (consulta != 1 and consulta != 2 and consulta != 3 and consulta != 4):
            print('Opção inválida')
            continue
        # D.a.VI - Retornar ao sistema
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
        else: #TODO
            print('Consulta por autor') #ERASE

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
            print('Opção inválida, digite novamente')
            continue
        for dic in lista_livro:
            if (inp_id == dic['id']):
                print('id: ', dic['id'])
                print('nome: ', dic['nome'])
                print('autor: ', dic['autor'])
                print('editora: ', dic['editora'])
        break





# CÓDIGO PRINCIPAL / MAIN
# A - Print com mensagem de boas vidas e nome #OK
print('Bem vindo a Livraria da Jéssica Hara!')

# B - lista vazia lista_livro e variável id_global #OK
lista_livro = []
id_global = 0

# Escolha de serviço
while True: #OK
    # F - estrutura de menu
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    servico = int(input('>> '))# input escolha do servico

    if (servico != 1 and servico != 2 and servico != 3 and servico != 4):# F.V - opção inválida e continuação do menu #OK
        print('Opção inválida')
        continue #TODO VERIFICAR
    elif (servico == 4):# F.IV - encerrar programa #OK
        print('Saindo do sistema')
        break
    elif (servico == 1):# F.I - cadastro de livro #OK
        id_global += 1
        cadastrar_livro(id_global)
        continue
    elif (servico == 2):#TODO F.II - consulta de livro
        consultar_livro()
        #D.a.IV - voltar ao menu principal
        continue
        print('consulta')#ERASE
    elif (servico == 3):# F.III - remover livro
        print('remover')#ERASE
    break


print(f'{lista_livro}') #ERASE

'''
print('-' * 30)
lista_livro = []
dic_lista = {'id':1,'nome':'nome2','autor':'autor2','editora':'editora2'}
dic_lista2 = {'id':2,'nome':'nome4','autor':'autor4','editora':'editora4'}
lista_livro.append(dic_lista)
lista_livro.append(dic_lista2)

while True:
    consulta_id = int(input('Digite o id do livro: '))
    if (consulta_id <= 0):
        print('Opção inválida, digite novamente')
        continue
    for dic in lista_livro:
        if (consulta_id == dic['id']):
            print('id: ', dic['id'])
            print('nome: ', dic['nome'])
            print('autor: ', dic['autor'])
            print('editora: ', dic['editora'])
    continue
'''