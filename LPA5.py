# Tuplas
mochila = ('Machado', 'Bacon')
print(mochila) #print ('Machado', 'Bacon')
print(mochila[1]) #print Bacon

for item in mochila:
    print(f'Na minha mochila tem: {'item'}')

    # desempacotamento - soma os parâmetros passados
def soma (*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n')

# Listas
mochila = ['Machado', 'Bacon'] #print ['Machado', 'Bacon']
mochila[1] = 'Laranja' 
print('Lista: ', mochila) #print ['Machado', 'Laranja']

lista_original = [5, 7, 9, 11]
lista_referenciada = lista original # está referenciando ao endereço da lista_original, então recebe os mesmos parâmetros, "apontador", se mexer nos parâmetros da referenciada, atualiza a original

lista_original = [5, 7, 9, 11]
lista_referenciada = lista original[:] # cria uma cópia

    #String dentro de listas
mochila = ['Machado']
mochila[0][0] #'M'

for item in mochila:
    for letra in item:
        print(letra, end='') # end=' sem quebra de linha
    print()

    #Lista dentro de lista
mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
mochila[0][0] #'Cebola'
mochila[0][0][0] #'C'

    #Criar listas
item = []
mercado = []

for i in range(3):
    item.append(input('Nome do item: '))
    item.append(int(input('Quantidade: ')))
    item.append(float(input('Valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)


# Dicionários
mochila = {'Machado':1, 'Bacon':2} #primeiro palara chave, segundo é o dado
print(mochila['Machado']) #print 1

    #Lista com dicionários
games = []
game1 = {'nome:':'Super Mario', 'videogame':'Super Nintendo', 'ano':1997}
game2 = {'nome':'Zelda', 'videogame':'Nintendo 64', 'ano':1998}
game3 = {'nome':'Pokemon', 'videogame':'Game boy', 'ano':1999}
games = [game1, game2, game3]
print(games)

    #Dicionário com listas
games = {'Nome':['Super Mario', 'Zelda', 'Pokemon'],'videogame':['Super Nintendo', 'Nintendo 64', 'Game boy'],'ano':[1990,1998,1999]}
print(games)

# Médotos em strings
s1 = 'Algorítmos'

s1 = list('Algorítmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado
s1[0] = 'a'


