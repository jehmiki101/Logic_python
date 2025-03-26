lista_livro = []
dic_lista = {'id':'id1','nome':'nome1','autor':'autor1','editora':'editora1'}

dic_lista1 = {'id':'id2','nome':'nome2','autor3':'autor2'}
lista_livro = [dic_lista, dic_lista1]
print(lista_livro[1])
for dic in lista_livro:
    print(dic.get('id'))
    print(dic['nome'])
    items = dic.items()
    id = -1