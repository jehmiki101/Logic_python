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
    lista_livro = []
    global id_global
    id_global = 0
    
    while (id_global > 0):
        nome = lista_livro.append(input('Qual o nome do livro? '))
        lista_livro.append(input('Qual o autor do livro? '))
        lista_livro.append(input('Qual a editora do livro? '))
        id_global += id_global
        
    print(lista_livro)
    dic_livro = {'id':}
    return dic_livro


lista_livro = []
global id_global
id_global = 0

while (id_global >= 0):
    nome = lista_livro.append(input('Qual o nome do livro? '))
    lista_livro.append(input('Qual o autor do livro? '))
    lista_livro.append(input('Qual a editora do livro? '))
    id_global += id_global
    break
    
print(lista_livro)