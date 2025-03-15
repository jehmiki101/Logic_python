# Questão 01

# A - Print com Boas vindas
print('Bem-vindo a Loja da Jéssica Hara')
# B - Inputs de valor unitário de produto e quantidade
valor_unitario = int(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
# C - definições de variável (cálculo do valor total com base nos inputs)
total = valor_unitario * quantidade
# E - atribuição dos percentuais de desconto em cada intervalo de valores
if (total < 2500):
    total_desc = total
elif (total >= 2500 and total < 6000 ):
    valor_desc = 0.04
    total_desc = total - (total * valor_desc)
elif (total >= 6000 and total < 10000):
    valor_desc = 0.07
    total_desc = total - (total * valor_desc)
else:
    valor_desc = 0.11
    total_desc = total - (total * valor_desc)
# D - prints dos valores com e sem descontos calculados
print(f'O valor SEM desconto: R${total}')
print(f'O valor COM desconto: R${total_desc}')
