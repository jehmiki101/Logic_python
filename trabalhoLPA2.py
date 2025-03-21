# questão 03

# B - implementação da função escolha_servico
def escolha_servico():
    while True:
        # B.a - prompt de escolha de serviço, transformação de caractere para maiúscula e limpeza de espaço final
        servico = input('Entre com o tipo de serviço desejado: ').upper().strip()
        # B.c - validação de escolha válida e retorno ao prompt
        if (servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT'):
            print('Escolha inválida, entre com o tipo do serviço novamente')
            continue
        # B.b - valor do serviço
        total_valor_serv = valores_servico(servico)
        return total_valor_serv
    
# função de especificação de valores por serviço
def valores_servico(sigla):
    val_serv = 0.2
    if (sigla == 'DIG'):
        val_serv = 1.1
    elif (sigla == 'ICO'):
        val_serv = 1
    elif (sigla == 'IPB'):
        val_serv = 0.4
    return val_serv

# C - função de cálculo de número de páginas
def num_pagina():
    while True:
        try:
            # C.a/C.c - input de número de páginas e retorno ao input se houver erro na resposta
            paginas = int(input('Entre com o número de páginas: '))
            if (paginas > 19999): # verificação de número de páginas acima de 20000
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                continue
            elif (paginas < 0): # verificação de número de páginas abaixo de zero
                print('Número de páginas abaixo de zero.')
                print('Por favor, entre com o número de páginas novamente.')
                continue
  
        except ValueError: # verificação de número de páginas inválido
            print('Número de páginas não identificado, entre com o número de páginas novamente.')
            continue

        percentual_desconto = desconto(paginas)
        # cálculo do serviço, quantidade de páginas vezes o tipo de serviço menos o desconto
        qnt_paginas_desc = paginas * percentual_desconto
        return qnt_paginas_desc

# C.b - função de especificação de desconto por número de páginas
def desconto(pg):
    desc = 0
    if (pg >= 20 and pg < 200):
        desc = 0.15
    elif (pg >= 200 and pg < 2000):
        desc = 0.20
    elif (pg >= 2000 and pg < 20000):
        desc = 0.25
    return 1 - desc


# CÓDIGO PRINCIPAL / MAIN
# A - print com a mensagem de boas vindas e nome, e lista de serviços
print('Bem vindo à copiadora da Jéssica Hara')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')

valor_adicional = 0

final_servico = escolha_servico()
qnt_paginas_desc = num_pagina()

# E - total a pagar
total_final = (final_servico * qnt_paginas_desc) + valor_adicional
print(f'Valor total final: R$ {total_final}')