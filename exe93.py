print("Cadastro de jogador de futebol")

cad = {}
partidas = []
cad['nome'] = input("Nome:")
total = int(input("Partidas jogadas:"))
for c in range(0, total):
    partidas.append(int(input(f"Quantos gols na partida {c+1}:")))
cad['gols'] = partidas[:]
cad['total'] = sum(partidas) #sum (somatório)
print("-=" * 30)
print(cad)
print("-=" * 30)
for k,v in cad.items():
    print(f"{k} = {v}")
print("-=" * 30)
print(f"O jogador {cad['nome']} jogou {total} partidas.")
for i, v in enumerate(cad['gols']): #enumerate pq é uma lista
    if v == 1:
        print(f"      => Na partida {i+1} fez {v} gol.")
    elif v == 0:
        print(f"      => Na partida {i+1} fez {v} gol.")
    else:
        print(f"      => Na partida {i+1} fez {v} gols.")
print(f"Foi um total de {cad['total']} gols.")



    

    
