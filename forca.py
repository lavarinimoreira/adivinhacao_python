#---------------------------------------------------------------------------+
#                                                                           #
#   forca.py                                                                #
#                                                                           #
#   Este programa tem como principal objetivo estudar as funcionalidades    #
#   da linguagem Python. Para tal, neste arquivo foi utilizado o conceito   #
#   do jogo da forca.                                                       #
#                                                                           #
#   Autor: Gabriel Lavarini <lavarinimoreira@gmail.com>                     #
#   github.com/lavarinimoreira                                              #
#                                                                           #
#---------------------------------------------------------------------------+

import random
def jogar():
    print("+-------------------------------+")
    print("#  Bem vindo ao jogo da Forca!  #")
    print("+-------------------------------+\n")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    indice_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice_aleatorio].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    erros = 0
    tentativas = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Forneça uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("A letra '{}' não está na palavra.".format(chute))
            print("{} tentativas restando.".format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print("\n",letras_acertadas, sep="")

    if(acertou):
        print("Ganhou!!")
    else:
        print("Perdeu =/")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()