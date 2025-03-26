item = []
mercado = []

for i in range(2):
    item.append(input('Nome do item: '))
    item.append(int(input('Quantidade: ')))
    item.append(float(input('Valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)