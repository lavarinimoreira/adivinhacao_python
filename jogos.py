#---------------------------------------------------------------------------+
#                                                                           #
#   jogos.py                                                                #
#                                                                           #
#   Este programa tem como principal objetivo estudar algumas das           #
#   funcionalidades da linguagem Python. Para tal foi utilizado o conceito  #
#   do jogo de adivinhação, que consiste na geração de um número aleatório  #
#   entre 1 e 100 que terá que ser decifrado por meio de tentativas como    #
#   também o conceito do jogo da forca.                                     #
#                                                                           #
#   Autor: Gabriel Lavarini <lavarinimoreira@gmail.com>                     #
#   github.com/lavarinimoreira                                              #
#                                                                           #
#---------------------------------------------------------------------------#

import forca
import adivinhacao

print("+----------------------------+")
print("#    Escolha o o seu jogo!   #")
print("+----------------------------+")

print("\n[1] - Forca\n[2] - Adivinhação\n[3] - Sair")

condicao = int(input("Selecione um jogo: "))

if(condicao == 1):
    print("Jogando forca")
    forca.jogar()
elif(condicao == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()

print("Encerrando programa.")