print('-' * 30)
lista_livro = []
dic_lista = {'id':1,'nome':'nome2','autor':'autor2','editora':'editora2'}
dic_lista2 = {'id':2,'nome':'nome4','autor':'autor2','editora':'editora4'}
lista_livro.append(dic_lista)
lista_livro.append(dic_lista2)


while True:
    inp_autor = input('Digite o Autor do livro: ')
    if (inp_autor == ''):
        print('Opção Inválida')
        continue
    for dic in lista_livro:
        dic.get('autor', inp_autor)
        print('id: ', dic['id'])
        print('nome: ', dic['nome'])
        print('autor: ', dic['autor'])
        print('editora: ', dic['editora'])
    break