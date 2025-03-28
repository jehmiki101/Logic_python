
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
        lista_livro.pop(index)