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
def jogar():
    print("+-------------------------------+")
    print("#  Bem vindo ao jogo da Forca!  #")
    print("+-------------------------------+\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou  = False

    while(not enforcou and not acertou):

        chute = input("Forneça uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra '{}' na posição {}".format(letra.upper(), index))
            index = index + 1

        print("jogando...")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()