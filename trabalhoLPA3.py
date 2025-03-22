# A - print com mensagem de boas vindas
print('Bem vindo a Livraria da Jéssica Hara!')


print('-' * 50)
print('-' * 17, 'MENU PRINCIPAL', '-' * 17)
print('Escolha a opção desejada: ')
print('1 - Cadastrar Livro')
print('2 - Consultar Livro(s)')
print('3 - Remover Livro')
print('4 - Sair')

# CÓDIGO PRINCIPAL / MAIN
cadastrar_livro()
print(lista_livro)

# B - lista vazia e variável
lista_livro = []
id_global = 0




# C - função 
def cadastrar_livro(id):
    nome = input('Qual o nome do livro? ')
    autor = input('Qual o autor do livro? ')
    editora = input('Qual a editora do livro? ')
    lista_livro = {'nome':nome, autor, editora}
    return dic_livro