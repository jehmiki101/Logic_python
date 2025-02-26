# Ecercício 01
x = 3
while (x < 13):
    print(f'{x}')
    x += 1

for i in range(3,13,1):
    print(f'{i}')

x = 0
while (x < 9):
    print(f'{x}')
    x += 2

for i in range(0,10,2):
    print(f'{i}')

# Exercício 02
print('LANCHONETE')
print('1 - Coxinha - R$5,00')
print('2 - Pastel - R$7,00')
print('3 - Café - R$4,00')
print('4 - Suco - R$6,00')
print('5 - Sair e finalizar compra')

total = 0

while True:
    produto = int(input('Digite o código do produto: '))
    if(produto == 1):
        quantidade = int(input('Digite a quantidade desejada: '))
        total = total + quantidade * 5.00
    elif(produto == 2):
        quantidade = int(input('Digite a quantidade desejada: '))
        total = total + quantidade * 7.00
    elif(produto == 3):
        quantidade = int(input('Digite a quantidade desejada: '))
        total = total + quantidade * 4.00
    elif(produto == 4):
        quantidade = int(input('Digite a quantidade desejada: '))
        total = total + quantidade * 6.00
    elif(produto == 5):
        print('Você finalizou a sua compra')
        break
    else:
        print('Produto inválido')
print(f'Total de: R${total}')

# Exercício 03
valor = int(input('Digite um valor: '))

while(valor > 0):
    if(valor >= 100):
        count100 = valor // 100
        valor = valor - count100 * 100
        print(f'Cédulas de 100: {count100}')
        if not valor:
            break
    elif(valor > 50):
        count50 = valor // 50
        valor = valor - count50 * 50
        print(f'Cédulas de 500: {count500}')
        if not valor:
            break
    elif(valor > 20):
        count20 = valor // 20
        valor = valor - count20 * 20
        print(f'Cédulas de 20: {count20}')
        if not valor:
            break
    elif(valor > 10):
        count10 = valor // 10
        valor = valor = count10 * 10
        print(f'Cédulas de 10: {count10}')
        if not valor:
            break
    elif(valor > 5):
        count5 = valor // 5
        valor = valor - count5 * 5
        print(f'Cédulas de 5: {count5}')
        if not valor:
            break
    elif(valor):
        count1 = valor
        print(f'Cédulas de 1: {count1}')


# Exercício 03
total = 0
valor_ing = 0
dinheiro = 0
qnt_idade = 0

while True:
    idade = int(input('Digite sua idade: '))
    if(idade == 0):
        break
    total += 1
    qnt_idade += idade
    if(idade < 3):
        valor_ing = 0
    else:
        if(idade > 12):
            valor_ing = 30
        else:
            valor_ing = 15
    dinheiro += valor_ing

if total > 0:
    media = qnt_idade / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Média de idades: {media}')