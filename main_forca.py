import jogo_forca as jf
import funcoes_forca as ff

def mostrar_menu():
    print('=' * 30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('=' * 30)

arquivo = 'score.txt'
if ff .existeArquivo(arquivo):
    print('Arquivo foi localizado no computador.')
else:
    print('Arquivo não existe.')
    ff.criarArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção (1/2/3): '))

    if (opcao == 1):
        print('Iniciar jogo!')
    elif (opção == 2):
        print('Score')
    elif (opcao == 3):
        print('Saindo do jogo. Até mais!')
        break
    else:
        print('Opção inválida. Tente outra.')