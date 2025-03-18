import desenhos_forca as df
import funcoes_forca as ff
from random import choice

def jogar():
    lista_palavras = list()
    arquivo = ff.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = df.imprimir_palavra_secreta(palavra_sorteada, acertos)
        #condição de vitória
        if (adivinha == palavra_sorteada):
            print('Você acertou!')
            break
        
        #tentativa
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if (tentativa in digitadas):
            print('Você já usou essa letra!')
            continue
        else:
            digitadas += tentativa #ou append
            if (tentativa in palavra_sorteada):
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')
        
        score = df.desenhar_forca(erros)

        #condição de fim de jogo
        if (erros == 6):
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada}.')
            break

    ff.inserir_score('score.txt', nome, score)