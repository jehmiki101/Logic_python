# C - função cadastrar livros
def cadastrar_livro(id):
    print('-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', '-' * 14)
    while True:
        print(f'Id do livro: {id}')
        nome = input('Qual o nome do livro? ')
        autor = input('Qual o autor do livro? ')
        editora = input('Qual a editora do livro? ')
        dic_lista = {'id':id,'nome':nome,'autor':autor,'editora':editora}
        print(f'{dic_lista}')
        global lista_livro
        lista_livro.append(dic_lista)
        return dic_lista


# CÓDIGO PRINCIPAL / MAIN
print('Bem vindo a Livraria da Jéssica Hara!')

# B - lista vazia e variável
lista_livro = []
id_global = 0

# Escolha de serviço
while True:
    # F - estrutura de menu
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    servico = int(input('>> '))# input escolha do servico

    if (servico != 1 and servico != 2 and servico != 3 and servico != 4):# F.V - opção inválida e continuação do menu
        print('Opção inválida')
        continue
    elif (servico == 4):# F.IV - encerrar programa
        print('Saindo do sistema')
        break
    elif (servico == 1):# F.I - cadastro de livro
        cadastrar_livro(id_global)
        id_global += 1
        continue
    elif (servico == 2):# F.II - consulta de livro
        print('consulta')
    elif (servico == 3):# F.III - remover livro
        print('remover')
    break


print(f'{lista_livro}')