nome_app = 'AdivinhaPy'
print("***********************")
print("Bem vindo ao " + nome_app)
print("***********************")

#   range(start, stop, step)

numero_secreto = 50
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute = int(input("Digite seu numero: "))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Acertou!")
    else:
        if(maior):
            print("Errou! Seu chute foi maior")
        elif(menor):
            print("Errou! Seu chute foi menor")

    rodada = rodada + 1
"""
if(numero_secreto == chute):
    print("Acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! Seu chute foi maior")
    if (chute < numero_secreto):
        print("Você errou! Seu chute foi Menor")
"""

print("Fim de jogo!")