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

def pedido ():
    while True:# D, G - Implementação de if/elif/else em modelo aninhado e While, break, continue
        valor_unidade = 0
        quantidade = 0
        global total# E - Acumulador para somatória de todos os valores

        sabor = input('Entre com o sabor desejado (CP ou AC): ')# Input sabor e validação
        if (sabor != 'CP' and sabor != 'AC'):
            print('Sabor inválido. Tente novamente', end='')
            continue

        tamanho = input('Entre com o tamanho desejado (P/M/G): ')# Input tamanho e validação
        if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
            print('Tamanho inválido. Tente novamente')
            continue

        if (sabor == 'CP'):# B - Escolha do sabor Cupuaçu
            if (tamanho == 'P'):# C - Escolha de tamanho P para Cupuaçu
                valor_unidade = 9
                print(f'Você pediu um Cupuaçu no tamanho P: R$', valor_unidade)
                total += valor_unidade
            elif (tamanho == 'M'):# C - Escolha de tamanho M para Cupuaçu
                valor_unidade = 14
                print(f'Você pediu um Cupuaçu no tamanho M: R$', valor_unidade)
                total += valor_unidade
            else:# C - Escolha de tamanho G para Cupuaçu
                valor_unidade = 18
                print(f'Você pediu um Cupuaçu no tamanho G: R$', valor_unidade)
                total += valor_unidade
        elif (sabor == 'AC'):# B - Escolha do sabor Açai
            if (tamanho == 'P'):# C - Escolha de tamanho P para Açai
                valor_unidade = 11
                print(f'Você pediu um Açaí no tamanho P: R$', valor_unidade)
                total += valor_unidade
            elif (tamanho == 'M'):# C - Escolha de tamanho M para Açai
                valor_unidade = 16
                print(f'Você pediu um Açaí no tamanho M: R$', valor_unidade)
                total += valor_unidade
            else:# C - Escolha de tamanho G para Açai
                valor_unidade = 20
                print(f'Você pediu um Açaí no tamanho G: R$', valor_unidade)
                total += valor_unidade
        break

total = 0
pedido()
adicao_pedido = input('Deseja mais alguma coisa? (S/N)')# F - Input adição de pedido
while (adicao_pedido == 'N'):
    break
while (adicao_pedido == 'S'):
    pedido()
    break
print(f'O valor total a ser pago: R${total}')
