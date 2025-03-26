lista_livro = []
dic_lista = {'id':'id1','nome':'nome1','autor':'autor1','editora':'editora1'}
dic_lista1 = {'id3':'id2','nome3':'nome2','autor3':'autor2','editora3':'editora2'}
lista_livro = [dic_lista, dic_lista1]
print(lista_livro)
for dic in lista_livro:
    for i in dic.items():
        print(f'{i}')