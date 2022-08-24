#---------------------------------------------------------------------------+
#                                                                           #
#   adivinhacao.py                                                          #
#                                                                           #
#   Este programa tem como principal objetivo estudar as funcionalidades    #
#   da linguagem Python. Para tal, neste arquivo foi utilizado o conceito   #
#   do jogo de adivinhação, que consiste na geração de um número aleatório  #
#   entre 1 e 100 que terá que ser decifrado por meio de tentativas.        #
#                                                                           #
#   Autor: Gabriel Lavarini <lavarinimoreira@gmail.com>                     #
#   github.com/lavarinimoreira                                              #
#                                                                           #
#---------------------------------------------------------------------------+
import random
def jogar():
    
    imprime_mensagem_inicial()
    nivel = nivel_dificuldade()

    numero_secreto = gera_numero_secreto()
    total_de_tentativas = switch_nivel(nivel)
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}.".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("\nVocê acertou na {}a tentativa!\nPontuação: {}\n".format(rodada,pontos))
            break
        else:
            if (maior):
                print("Você errou. O seu chute foi maior do que o número secreto.\n")
            elif(menor):
                print("Você errou. O seu chute foi menor do que o número secreto.\n")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
def imprime_mensagem_inicial():
    print("+-------------------------------------+")
    print("#  Bem vindo ao jogo de Adivinhação!  #")
    print("+-------------------------------------+\n")
def gera_numero_secreto():
    return random.randrange(1,101)
def nivel_dificuldade():
    print("[1] - Fácil\n[2] - Médio\n[3] - Difícil")
    nivel = int(input("Selecione o nível de dificuldade: "))
    if(nivel > 3 or nivel < 1):
        return 3 # Retornando o nível difícil caso a entrada de dados seja feita por um valor inválido...
    else:
        return nivel
def switch_nivel(nivel):
    total_de_tentativas = 5
    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    return total_de_tentativas

if(__name__ == "__main__"):
    jogar()
