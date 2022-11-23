def jogar():
    print("************************")
    print("***Bem vindo ao Forca***")
    print("************************")

    palavra_secreta = "banana"
    len_palavra = len(palavra_secreta)
    print(len_palavra)
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        #index = index.__add__()
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posicao {}".format(chute, index))

            index = index + 1

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()