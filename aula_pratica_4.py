# Docstring - Documentação interna
def soma3(x = 0, y = 0, z = 0):
    '''
    : param x: funcionamento de cada parâmetro
    : param y: funcionamento de cada parâmetro
    : param z: funcionamento de cada parâmetro
    
    '''
    return x+y+z
help(soma3) # interactive help

# Exercício 01
def fatorial(numero):
    '''
    Função que calcula a função fatorial de um número inteiro
    :param num:
    :return:
    '''
    fat = 1
    for i in range(1, numero + 1, 1):
        fat *= i
    print(f'O fatorial de {numero} é igual a {fat}.')

numero_inp = int(input('Digite um número: '))
fatorial(numero_inp)


# resolução
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial (num):
    '''
    :param num:
    :return:
    '''
    fat = 1
    if(num == 0):
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x = valida_int('Digite um número: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')


# Exercício 02
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideoGame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try: 
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if (existeArquivo(arquivo)):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar todos os itens')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if(op == 1):
        print('Opção de cadastro selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideoGame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
    elif(op == 2):
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif(op == 3):
        print('Encerrando o programa...')
        break