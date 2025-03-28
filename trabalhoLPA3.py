# REFATORAÇÃO PRINTS
def invalido():
    print('Opção Inválida')


# C - Função cadastrar livros #OK
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

# D - Função de consulta de livro#OK
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
            print('Voltando ao menu principal') #TODO
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

# D.a - Menu consultar livro#OK
def menu_consultar():
    print('-' * 50)
    print('-' * 14, 'MENU CONSULTAR LIVRO', '-' * 14)
    print('Escolha a opção desejada: ')
    print('1 - Consultar Todos')
    print('2 - Consultar por Id')
    print('3 - Consultar por Autor')
    print('4 - Retornar ao menu')

# D.a.I - função consultar todos os livros cadastrados#OK
def consulta_geral():
    print('-' * 30)
    global lista_livro
    for dic in lista_livro:
        print('id: ', dic['id'])
        print('nome: ', dic['nome'])
        print('autor: ', dic['autor'])
        print('editora: ', dic['editora'])
        print(' ')

# D.a.II - Consultar livro por Id #OK
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

# D.a.III - Consultar livro por Autor #OK
def consulta_autor():
    print('-' * 30)
    global lista_livro
    while True:
        inp_autor = input('Digite o Autor do livro: ')
        if (inp_autor == ''):
            invalido()
            continue
        for dic in lista_livro:
            if (dic.get('autor') == inp_autor):
                print('id: ', dic['id'])
                print('nome: ', dic['nome'])
                print('autor: ', dic['autor'])
                print('editora: ', dic['editora'])
                break
        else:
            invalido()
        break


# E - Função de remover livros #TODO
def remover_livro():
    while True:
        print('-' * 50)
        print('-' * 15, 'MENU REMOVER LIVRO', '-' * 15)
        inp_remove = int(input('Digite o id do livro a ser removido: '))
        if (inp_remove == ''):
            invalido()
            continue
        for dic in lista_livro:
            if (dic.get('id') == inp_remove):
                dic.clear()
                print('Livro removido com sucesso!')
                break
        else:
            print('Id inválido')
        break





# CÓDIGO PRINCIPAL / MAIN
# A - Print com mensagem de boas vidas e nome #OK
print('Bem vindo a Livraria da Jéssica Hara!')

# B - lista vazia lista_livro e variável id_global #OK
lista_livro = []
id_global = 0

# Escolha de serviço
while True: #OK
    # F - estrutura do menu principal
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    servico = int(input('>> '))# input escolha do servico

    if (servico != 1 and servico != 2 and servico != 3 and servico != 4):# F.V - opção inválida e continuação do menu #OK
        invalido()
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
    elif (servico == 3):# F.III - remover livro
        remover_livro()
        continue
    break


print(f'{lista_livro}') #ERASE



def invalido():
    print('Opção Inválida')
print('-' * 30)
lista_livro = []
dic_lista = {'id':1,'nome':'nome2','autor':'autor2','editora':'editora2'}
dic_lista2 = {'id':2,'nome':'nome4','autor':'autor2','editora':'editora4'}
lista_livro.append(dic_lista)
lista_livro.append(dic_lista2)
print(lista_livro)

while True:
    inp_remove = int(input('Digite o id do livro a ser removido: '))
    if (inp_remove == ''):
        invalido()
        continue
    index = 0

    # if (inp_remove <= len(lista_livro)):
    for i in lista_livro:
        if (i.get('id') == inp_remove):
            index = i
            print(index)

    for dic in range(len(lista_livro)):
        index = dic
        print(index)
        lista_livro.pop(index)
    break



print(lista_livro)



'''        if (dic.get('id') == inp_remove):
            index 