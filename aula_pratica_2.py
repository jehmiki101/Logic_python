# Exercício explressão booleanas
if(2 + 2 < 4):
if(7 // 3 == 1 + 1):
if((3 ** 2) + (4 ** 2) == 25):
if((2 + 4 + 6) > 12):
if(1387 % 19 == 0):
if(31 % 2 == 0):
if(min(34, 29, 31) < 30):

# Condicional simples
idade = int(input('Digite sua idade: '))
if(idade > 60):
    print('Você tem direito aos benefícios')

dano = int(input('Digite seu dano: '))
escudo = int(input('Digite seu escudo: '))
if(dano > 10 and escudo == 0):
    print('Você está morto!')

norte = True
sul = False
leste = False
oeste = False
if(norte or sul or leste or oeste == True):
    print('Você escapou!')

# Condicional composta
ano = 2006
if(ano % 4 == 0):
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

x = True
y = False
if(x and y == True):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')

# Exercício 01
lado_01 = int(input('Digite o primeiro lado do triângulo: '))
lado_02 = int(input('Digite o segundo lado do triângulo: '))
lado_03 = int(input('Digite o terceiro lado do triângulo: '))
if((lado_01 and lado_02 and lado_03 > 0) and (lado_01 + lado_02 > lado_03) and (lado_03 + lado_02 > lado_01) and (lado_01 + lado_03 > lado_02)):
    if(lado_01 == lado_02 == lado_03):
        print('O triângulo é equilátero')
    elif(lado_01 != lado_02 != lado_03):
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print('Ao menos um dos valores indidados não serve para formar um triângulo')

# Exercício 02
print('Calculadora')
print('+')
print('-')
print('*')
print('/')
operacao = input('Qual operador deseja utilizar?')
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

if(operacao == '+'):
    print(f'O resultado de {x} + {y} é: {x + y}')
elif(operacao == '-'):
    print(f'O resultado de {x} - {y} é: {x - y}')
elif(operacao == '*'):
    print(f'O resultado de {x} * {y} é: {x * y}')
elif(operacao == '/'):
    print(f'O resultado de {x} / {y} é: {x / y}')
else:
    print('Encerrando o programa...')

# Exercício 03
kwh = float(input('Qual a quantidade de kWh consumida:'))
inst = input('Qual o tipo de instalação? (R, I ou C)')

if(inst == 'R'):
    if(kwh >= 500):
        preco = 0.65
    else:
        preco = 0.4
    print(f'Total a pagar: {kwh * preco}')
elif(inst == 'C'):
    if(kwh >= 1000):
        preco = 0.60
    else:
        preco = 0.55
    print(f'Total a pagar: {kwh * preco}')
elif(inst == 'I'):
    if(kwh >= 5000):
        preco = 0.60
    else:
        preco = 0.55
    print(f'Total a pagar: {kwh * preco}')
else:
    print('Instalação inválida. Encerrando...')