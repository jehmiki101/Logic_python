# Parâmetro
def realce(s1):
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
    print(s1) 
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')

realce('          MENU')

# 02 parâmetros
# precisa passar os dois valores obrigatóriamente
def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7)

#  Parâmetros opcionais
# parâmetros default
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1, 2, 3)
soma3(1, 2) # z foi omitido
soma3(1)    # y e z foram omitidos
soma3()

# Exercício 01

def placa(len, word):
    print('+', '-' * len, '+')
    print('|', word, '|')
    print('+', '-' * len, '+')

word_inp = input('Digite uma palavra: ')
len_inp = len(word_inp)

placa(len_inp, word_inp)

# Resolução
def borda(s1):
    tam = len(s1)
    if (tam):
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

word_inp = input('Digite uma palavra: ')
borda(word_inp)



# Escopo
def omelete():
    global ovos
    ovos = 6

ovos = 12
omelete()
print(ovos)

# Retorno
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma3(1, 2, 3)
print(retornado)
# ou
print(soma3(2,2))


# Exercício 02
def string(len, min, max):
    if(len > 0):
        if(min < len < max):
            print('Tamanho da string aceita')
            return True
        else:
            print('Tamanho da string recusada')
            return False

word_inp = input('Digite uma palavra: ')
string(len(word_inp), 2, 5)


# Erros , try/except
def div():
    try:
        num1 = int(input('Digite um número: ')) 
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('OOps')
    except: # engloba todos os erros
        print('Algo errado aconteceu')
    else:
        return res
    finally:
        print('Executa sempre')

print(div())

# Exercício 03
calc = lambda x, y: (x + 5) * y
print(calc(5, 10))