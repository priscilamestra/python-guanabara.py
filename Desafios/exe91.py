print("Jogo de dados em python")
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "Jogador1": randint(1,6),"Jogador2": randint(1,6), "Jogador3": randint(1,6),"Jogador4": randint(1,6),
     "Jogador5": randint(1,6), "Jogador6": randint(1,6)
}
ranking = []
print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #ordenar o jogo.items #(1) = valor de 1 a 6
print('-=' *24)
print("=== RANKING DOS JOGADORES ===")
for i, v in enumerate(ranking): # enumerate pq é lista
    print(f"{i+1}° lugar: {v[0]} com {v[1]}.") #tupla dentro de uma lista, v[0] [('jogador1')], v[1] valor.
    sleep(1)

