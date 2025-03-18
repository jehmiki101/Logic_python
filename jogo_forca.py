import funcoes_forca as ff
from random import choice

def jogar():
    lista_palavras = list()
    arquivo = ff.abrirArquivoLeitura('palavra.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

palavra_sorteada = choice(lista_palavras)

for x in range(50):
    