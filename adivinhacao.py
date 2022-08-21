
import random
def jogar_adivinhacao():
    print("+-------------------------------------+")
    print("#  Bem vindo ao jogo de Adivinhação!  #")
    print("+-------------------------------------+\n")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("[1] - Fácil\n[2] - Médio\n[3] - Difícil")
    nivel = int(input("Selecione o nível de dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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

    print("Fim do jogo")