# A - print com mensagem de boas vindas
def menu():
    print('-' * 50)
    print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')

# B - lista vazia e variável
# lista_livro = []


def escolha_servico():
    while True:
        menu()
        servico = input('>>')
        if (servico != '1' and servico != '2' and servico != '3'):
            print('Escolha inválida')
            continue
        elif (servico == '4'):
            print('Saindo do sistema')
            break
        elif (servico == '1'):
            cadastrar_livro()
            continue
        return servico



# C - função cadastrar livros
def cadastrar_livro():
    print('-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', '-' * 14)
    while True:
        global id_global
        id_global += id_global
        print(f'Id do livro: {id_global}')
        dic_lista = {}
        nome = input('Qual o nome do livro? ')
        autor = input('Qual o autor do livro? ')
        editora = input('Qual a editora do livro? ')

        dic_lista[id_global] = nome, autor, editora
        print(f'{dic_lista}')
        break
    
# CÓDIGO PRINCIPAL / MAIN
print('Bem vindo a Livraria da Jéssica Hara!')
escolha_servico()
id_global = 0

# print(lista_livro)