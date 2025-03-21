# questão 03

# B - implementação da função escolha_servico
def escolha_servico():
    # prompt de escolha de serviço, transformação de caractere para maiúscula e limpeza de espaço final
    servico = input('Entre com o tipo de serviço desejado: ').upper().strip()

    servicoValido = valida_servico(servico)    
    if (servicoValido):
        valores_servico(servico)
        num_pagina()

def valida_servico(servico):
    # verificação de serviço solicitado pelo usuário inválido
    if (servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT'):
        print('Escolha inválida, entre com o tipo do serviço novamente')
        return False
    return True

    
# função de especificação de valores por serviço
def valores_servico(sigla):
    global val_serv
    if (sigla == 'DIG'):
        val_serv = 1.1
    elif (sigla == 'ICO'):
        val_serv = 1
    elif (sigla == 'IPB'):
        val_serv = 0.4
    else:
        val_serv = 0.2
    print(f'O valor do serviço é de R$ {val_serv} por página')

# C - função de cálculo de número de páginas
def num_pagina():
    paginas = input('Entre com o número de páginas: ')



# A - print com a mensagem de boas vindas e nome, e lista de serviços
print('Bem vindo à copiadora da Jéssica Hara')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')

val_serv = 0
escolha_servico()