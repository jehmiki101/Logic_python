# Expressões algébricas
print(1 + 2 + 3 + 4 + 5)

print((23 + 19 + 31) / 3)

print(403 // 73)

print(403 % 73)

print(2 ** 10)

print(abs(54 - 57))

print(min(34, 29, 31))

# Atribuição
a = 3
b = 4
c = a * a + b * b
print(c)

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + ' ' + s2 + ' ' + s3)
print((s1 + ' ') * 10)
print((s1 + ' ') + (s2 + ' ')* 2 + (s3 + ' ') * 3)
print((s1 + ' ' + s2 + ' ') * 7)
print((s2 + s2 + s3 + ' ') * 5)

# Problemas exercício 1
preco = float(input('Digite o preço do procuto: '))
percentual = float(input('Digite o percentual de desconto a ser aplicado(0-100%): '))
desconto = preco * (percentual / 100)
preco_final = preco - desconto
print(f'O valor do deconto de {percentual}% aplicado no preço de {preco} será de {desconto}, o valor final será: {preco_final}')

# Problemas exercício 2
km_percorrido = float(input('Digite a quantidade de quilômetros percorridos: '))
quant_dias = int(input('Digite a quantidade de dias utilizados: '))
valor_diaria = quant_dias * 60
valor_km = km_percorrido * 0.15
soma = valor_diaria + valor_km
print(f'O valor a ser pago é de: R${valor_diaria} pelos dias utilizados mais R${valor_km} pelos quilômetros percorridos, total de R${soma}')

# Problemas exercício 3
frase = input('Digite uma frase: ')
tam = len(frase)
frase_metade = frase[:int(tam/2)]
print(frase_metade[-2:])