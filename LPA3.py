# While

x = 1
while (x <= 5):
    print(x)
    x = x + 1

# --
inicial = int(input('Valor inicial: '))
final = int(input('Valor final: '))

x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1

# --
soma = 0
cont = 1
while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma += x
    cont += 1
media = soma / 5
print(f'Média final: {media}')

# -- Loop com print
x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print(f'Você digitou {x}. Encerrando o programa...')

# -- Break
print('Digite um texto: ')
print('Para encerrar escreva "sair".')
while True:
    texto = input('')
    print(texto)
    if (texto == 'sair'):
        break
print('Encerrando o programa...')

# -- Continue
while True:
    nome = input('QUal o seu nome? ')
    if (nome != 'Lenhadorzinho'):
        continue
    senha = input('Qual a sua senha? ')
    if (senha == 'UnInter'):
        break
    print('Acesso concedido')

# --Truthy/Falsey
nome = ''
while not nome:
    nome = input('Digite seu nome: ')

valor = int(input('Digite um número qualquer: '))
if valor:
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')

# For
for i in range(6):
    print(i)

for i in range(0,6,2):
    print(i)

frase = 'Lógica de Programação e Algoritmos'
for i in range(0, len(frase), 1):
    print(frase[i], end="")

# Exercício
soma = 0
qnt = 0
for i in range(1,101):
    if(i % 2 == 0):
        soma += i
        qnt += 1
media = soma / qnt
print(media)

# Exercício 02
# -- 2 whiles
tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}:')
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1

# --2 for
tabuada = 1
for i in range(0,10,1):
    print(f'TABUADA DO {tabuada}:')
    i = 1
    for i in range(0,11,1):
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1
