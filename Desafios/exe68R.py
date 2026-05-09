print("Jogo do par ou ímpar.")
from random import randint
vezes = 0 #vezes tem que estar fora do laço para contar as vitórias
while True:
    total = 0
    pc = randint(0,10)
    jogador = int(input("Digite um valor:"))
    total = jogador + pc
    tipo = input("Par ou Ìmpar [P/I]:").strip().upper()[0] #pegar só a primeira letra
    while tipo not in "PpIi":
        tipo = input("Jogada inválida. Par ou Ímpar ? [P/I]:").strip().upper()[0] 
    print(f"Você jogou {jogador} e o computador jogou {pc}. Total foi de {total} então é", end = " ")
    print("par." if total % 2 == 0 else "ímpar.") #rever como fazer de outra forma
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceeeeu mané.")
            vezes = vezes + 1
        else:
            print(f"Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceeeeu mané.")
            vezes = vezes + 1
        else:
            print(f"Você perdeu!")
            break
    print("Vamos jogar de novo ...")
if vezes == 1:
    print(f"GAME OVER, você venceu {vezes} vez.")
else:
    print(f"GAME OVER, você venceu {vezes} vezes.")


