print("***********************")
print("Bem vindo ao AdivinhaPy")
print("***********************")

numero_secreto = 50

chute_srt = input("Digite seu numero: ")

chute = int(chute_srt)

if(numero_secreto == chute):
    print("Acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! Seu chute foi maior")
    if (chute < numero_secreto):
        print("Você errou! Seu chute foi Menor")

print("Fim de jogo!")