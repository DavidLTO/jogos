import adivinhacao
import forca

print("************************")
print("*****Escolha o Jogo*****")
print("************************")

print("(1)Forca, (2)Adivinhação")

jogo = int(input("Selecione o jogo: "))

if(jogo ==1):
    forca.jogar()
elif(jogo ==2):
    adivinhacao.jogar()