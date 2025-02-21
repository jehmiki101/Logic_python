frase = input('Digite uma frase: ')
tam = len(frase)
frase_metade = frase[:int(tam/2)]
print(frase_metade[-2:])