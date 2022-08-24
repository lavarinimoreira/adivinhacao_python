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

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou  = False
    erros = 0
    tentativas = 6

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("A letra '{}' não está na palavra.".format(chute))
            print("{} tentativas restando.".format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print("\n",letras_acertadas, sep="")

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

#---------------------------------------+
#   Definindo as funções do programa    #
#---------------------------------------+
def imprime_mensagem_abertura():
    print("+-------------------------------+")
    print("#  Bem vindo ao jogo da Forca!  #")
    print("+-------------------------------+\n")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    indice_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice_aleatorio].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def pede_chute():
    chute = input("Forneça uma letra: ")
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def imprime_mensagem_vencedor():
    print("Ganhou =)")
def imprime_mensagem_perdedor():
    print("Perdeu =/")

if(__name__ == "__main__"):
    jogar()
