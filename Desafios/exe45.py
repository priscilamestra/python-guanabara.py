print("{:^40}" .format("PEDRA, PAPEL E TESOURA"))
from random import randint 
from time import sleep

itens = ("Pedra", "papel", "tesoura")
computador = randint(0, 2)

print("Suas opções:")
print("[0] {}PEDRA{}" .format("\033[1m", "\033[m"))
print("[1] {}PAPEL{}" .format("\033[1m", "\033[m"))
print("[2] {}TESOURA{}" .format("\033[1m", "\033[m"))
jogador = int(input("Qual é a sua jogada?"))
while jogador < 0 or jogador > 2:
    jogador = int(input("Jogada inválida. Jogue de novo:"))
print("""{}JO{}
{}KEN{}
{}PO{}""" .format("\033[1;35m", "\033[m", "\033[1;36m", "\033[m", "\033[1;33m", "\033[m"))    
sleep(1)
print("Jogador escolheu {}{}{}." .format("\033[1m",itens[jogador],"\033[m"))
print("Computador escolheu {}{}{}." .format("\033[1m",itens[computador],"\033[m"))

if computador == 0:
    if jogador == 0:
        print("{}EMPATE{}" .format("\033[1;34m", "\033[m"))
    elif jogador == 1:
        print("Jogador {}venceu{}!" .format("\033[1;32m", "\033[m"))
    elif jogador == 2:
        print("Computador {}venceu{}!" .format("\033[1;32m", "\033[m"))

elif computador == 1:
    if jogador == 1:
        print("{}EMPATE{}" .format("\033[1,34m", "\033[m"))
    elif jogador == 0:
        print("Computador {}ganhou{}!" .format("\033[1;32m", "\033[m"))
    elif jogador == 2:
        print("Jogador {}ganhou{}!" .format("\033[1;32m", "\033[m"))

elif computador == 2:
    if jogador == 2:
        print("{}EMPATE{}" .format("\033[;34m", "\033[m"))
    elif jogador == 0:
        print("Jogador {}ganhou{}!" .format("\033[1;32m", "\033[m"))
    elif jogador == 1:
        print("Computador {}ganhou{}!" .format("\033[1;32m", "\033[m"))
input() 