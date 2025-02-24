# Aula 02
# Exercício 01
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
if(x == y):
    print(f'Os números {x} e {y} são iguais')
if(x > y):
    print(f'O número {x} é maio que o número {y}')
else:
    print(f'O número {x} é menor que o número {y}')

# Exercício 02
x = int(input('Digite um número: '))
if(x % 2 == 0):
    print(f'O número {x} é par')
else:
    print(f'O número {x} é ímpar')

# Operadores Lógicos
print(not x)
print(x and Y)
print(x or y)

# Exercício 03
materia_01 = float(input('Média da matéria 01: '))
materia_02 = float(input('Média da matéria 02: '))
materia_03 = float(input('Média da matéria 03: '))
if(materia_01 and materia_02 and materia_03 <= 7):
    print('O aluno passou de ano')
else:
    print('O aluno não passou de ano')

# Exercício 04
print('Escolha o que quer comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha: '))
quantidade = int(input('Quantas unidades? '))
if(produto == 1):
    pagar = quantidade * 2.3
    print(f'Você comprou {quantidade} de maçãs. Total à pagar: {pagar}')
elif(produto == 2):
    pagar = quantidade * 3.6
    print(f'Você comprou {quantidade} de laranjas. Total à pagar: {pagar}')
elif(produto == 3):
    pagar = quantidade * 1.85
    print(f'Você comprou {quantidade} de bananas. Total à pagar: {pagar}')
else:
    print('Produto inexistente!')

# Exercício 05
nome = input('Digite seu nome: ')
if(nome == 'Vinicius'):
    print('Olá, Vinicius')
else:
    idade = int(input('Digite sua idade: '))
    if(idade < 18):
        print('Você não é o Vinicius, e é menor de idade.')
    elif(idade > 100):
        print('Você não é o Vinicius, e possivelmente não existe')
