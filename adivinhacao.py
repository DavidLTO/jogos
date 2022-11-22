import random
def jogar():
    print("************************")
    print("Bem vindo ao Adivinhação")
    print("************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    rodada = 1

    print("Escolha o nível (1) Facil, (2) Medio, (3) Dificil")
    nivel = int(input("Qual nível quer jogar?" ))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    while(rodada <= total_tentativas):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute = int(input("Digite seu numero: "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Acertou!")
            break
        else:
            if(maior):
                print("Errou! Seu chute foi maior")
            elif(menor):
                print("Errou! Seu chute foi menor")

        rodada = rodada + 1

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()