print('Olá, mundo!')
print(2+3)
print('O resultado da soma de 2+3 é', 2+3)

nota = 8.5
disciplina = 'Lógica de Programação e Algorítimos'

print(nota)
print(disciplina)

# variáveis
a = 1
b = 5

resposta = a == b
print(resposta)

# arrays
frase = 'Olá, mundo!'
print(frase[2])

# concatenação
s1 = 'Lógica de Programação'
s1 = s1 + ' e Algorítmos'
print(s1)

# repetindo strings
s1 = 'A' + '-' * 10 + 'B'
print(s1)

# marcador de posição
nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1)

nota = 8.5
disciplina = 'Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1)

# fatiamento, digito final precisa ser +1
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
print(s1[:6])

# tamanho
tamanho = len(S1)

# input
idade = input('Qual sua idade?')
print(idade)

nome = input('Qual sua nome?')
print(f'Olá {nome}, seja bem-vindo!')

# casting
nota = float(input('Qual nota você recebeu na disciplina? '))
print(f'você tirou nota {nota}.')

# exercício
x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
resposta = f'O resultado da soma de {x} com {y} é {x + y}'
print(resposta)