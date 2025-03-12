import math as m
from math import sqrt

print(m.sqrt(9))


# Exercício 01
notas = [9,7,7,10,3,9,6,6,2]
notas[-1] = 4
print(notas.count(7))
print(max(notas))
notas.sort() #ordena
print(notas)

notas = [9,7,7,10,3,9,6,6,2]
print(sum(notas)/len(notas))

# Exercício 02
palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')
for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for letra in palavra:
        if(letra.lower()) in 'aeiou':
            print(letra.upper(), end=' ')

# Exercício 03
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

print('Jokempo')
print('1-Pedra')
print('2-Papel')
print('3-Tesoura')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1,j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print(f'Número de vitórias do jogador 1: {resultados[0]}')
print(f'Número de vitórias do jogador 2: {resultados[1]}')
print(f'Número de EMPATES: {resultados[2]}')

# Exercício 04
import math
cadastro = {'nome':[], 'sexo':[], 'ano':[]}
while True:
    terminar = input('Deseja cadastrar uma pessoa: [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)
