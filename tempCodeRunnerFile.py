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
    try:
        inp_remove = int(input('Digite o id do livro a ser removido: '))
        if (inp_remove <= len(lista_livro) and inp_remove > 0):
            index = 0
            for i in range(len(lista_livro)):
                if (lista_livro[i].get('id') == inp_remove):
                    index = i
            lista_livro.pop(index)
        else:
            invalido()
    except:
        print('Id inválido')