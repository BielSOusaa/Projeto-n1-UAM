from random import randint

sala = 1
caminho = 0
jogadas = 0


print("\nHoje você será o líder de uma guilda de heróis! Como todo bom líder, você deverá guiar os guerreiros através do labirinto.\n")

while sala < 9 and jogadas < 7:
    caminho = int(input("Qual caminho você seguirá ?\n[1] Vermelho\n[2] Preto\nEscolha : "))
    if(sala == 8 and caminho == 2):
        print("\nVocê acaba de entrar um portal! O portal te teletransporta aleatoriamente para uma sala\n") 
        sala = randint(1,5)
    elif(sala == 6):
        sala += 2
        print ("Da sala 6 foi enviado automaticamente para a sala 8!".format(sala))
    elif(caminho == 1 or caminho == 2):
        sala += caminho
    else:
        print("Numero inválido!")
    print("\nSua sala atual é : {}\n".format(sala))
    jogadas = jogadas + 1
if(sala == 9):
    print("Você venceu! Parabens por chegar na sala 9 !!!")
elif(jogadas >= 7):
    print("Você perdeu por excesso de jogadas!")
print("Total de jogadas : {}\n".format(jogadas))
