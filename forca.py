def jogar():
    print("************************")
    print("***Bem vindo ao Forca***")
    print("************************")

    palavra_secreta = "banana".upper()
    letras_corretas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_corretas[index] = letra
                    print("A letra {} na posicao {}".format(chute, index))

                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_corretas

        print(letras_corretas)
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("*** Fim de jogo! ***")

if (__name__ == "__main__"):
    jogar()
