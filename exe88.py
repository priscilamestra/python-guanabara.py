from random import randint
from time import sleep 
lista = []
jogos = []
print("-"*19)
print("JOGO DA MEGA SENA")
print("-"*19)

quantidade = int(input("Quantos jogos você quer gerar?"))
total = 1 # total de vezes que ele vai sortiar os jogos
while total <= quantidade: #enquanto o total for igual ou menor que quantidade
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista: # se o num não estiver em lista, eu adiciono ele na lista
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1 
print(f"======= SORTEANDO {quantidade} JOGOS =======")
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")
    sleep(1)

   