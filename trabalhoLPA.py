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


# Questão 02

# A - Print com Boas vindas e cardápio
print('Bem-vindo a Loja De açaí e cupuaçu da Jéssica Hara!')
print('-' * 20, 'Cardápio', '-' * 20)
print('-' * 50)
print('---', '|', ' Tamanho ', '|', ' Cupuaçu(CP) ', '|', ' Açaí(AC) ', '|', '---')
print('---', '|', '    P    ', '|', '  R$  9,00   ', '|', ' R$ 11,00 ', '|', '---')
print('---', '|', '    M    ', '|', '  R$ 14,00   ', '|', ' R$ 16,00 ', '|', '---')
print('---', '|', '    G    ', '|', '  R$ 18,00   ', '|', ' R$ 20,00 ', '|', '---')
print('-' * 50)

# B - Input de sabor

def pedido ():
    while True:
        sabor = input('Entre com o sabor desejado (CP ou AC): ')
        valor_unidade = 0
        quantidade = 0
        total = 0
        if (sabor == 'CP'):
            tamanho = input('Entre com o tamanho desejado (P/M/G): ')
            if (tamanho == 'P'):
                valor_unidade = 9
                quantidade += 1
                print(f'Você pediu um Cupuaçu no tamanho P: R$', valor_unidade)
            elif (tamanho == 'M'):
                valor_unidade = 14
                quantidade += 1
                print(f'Você pediu um Cupuaçu no tamanho M: R$', valor_unidade)
            elif (tamanho == 'G'):
                valor_unidade = 18
                quantidade += 1
                print(f'Você pediu um Cupuaçu no tamanho G: R$', valor_unidade)
            else:
                print('Tamanho inválido, tente novamente')
                break
        elif (sabor == 'AC'):
            tamanho = input('Entre com o tamanho desejado (P/M/G): ')
            if (tamanho == 'P'):
                valor_unidade = 11
                quantidade += 1
                print(f'Você pediu um Açaí no tamanho P: R$', valor_unidade)
            elif (tamanho == 'M'):
                valor_unidade = 16
                quantidade += 1
                print(f'Você pediu um Açaí no tamanho M: R$', valor_unidade)
            elif (tamanho == 'G'):
                valor_unidade = 20
                quantidade += 1
                print(f'Você pediu um Açaí no tamanho G: R$', valor_unidade)
            else:
                print('Tamanho inválido, tente novamente')
                break
        else:
            print('Sabor inválido. Tente novamente')
        total += valor_unidade
        break

pedido()
adicao_pedido = input('Deseja mais alguma coisa? (S/N)')
pedido()
