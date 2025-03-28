print('-' * 30)
lista_livro = []
dic_lista = {'id':1,'nome':'nome2','autor':'autor2','editora':'editora2'}
dic_lista2 = {'id':2,'nome':'nome4','autor':'autor4','editora':'editora4'}
lista_livro.append(dic_lista)
lista_livro.append(dic_lista2)

while True:
    consulta_id = int(input('Digite o id do livro: '))
    if (consulta_id <= 0):
        print('Opção inválida, digite novamente')
        continue
    for dic in lista_livro:
        if (consulta_id == dic['id']):
            print('id: ', dic['id'])
            print('nome: ', dic['nome'])
            print('autor: ', dic['autor'])
            print('editora: ', dic['editora'])
    continue