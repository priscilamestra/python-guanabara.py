print("Aprimorando os dicionários")

cad = {}
partidas = []
time = []
media = 0
while True:
    cad.clear()
    cad['nome'] = input("Nome:")
    cad['sexo'] = input("Sexo [F/M]:").upper()[0]
    while cad['sexo'] not in "FM":
        cad['sexo'] = input("Respota inválida. Sexo [F/M]:").upper()[0]
    total = int(input(f"Partidas jogadas por {cad['nome']}:"))
    partidas.clear()
    for c in range(0,total):
        partidas.append(int(input(f"Quantos gols na partida {c+1}:")))
    cad['gols'] = partidas[:]
    cad['total'] = sum(partidas)
    cad['média'] = sum(partidas)/ total
    time.append(cad.copy())
    resp = input("Deseja continuar? [S/N]:").upper()
    while resp not in "SsNn":
        resp = input("Respota inválida. Deseja continuar? [S/N]:").upper()
    if resp in "nN":
        break
print("-=" * 30)
print("  cod ", end="")
for i in cad.keys(): 
    print(f" {i:<10} ", end="")
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>4}   ', end="")
    for d in v.values():
        print(f"{str(d):<12}", end='')
    print()
print("-" * 60)
while True:
    busca = int(input("Digite o indice do jogador que deseja ver os dados:"))
    while busca > len(time)-1:
        busca = int(input("Resposta inválida, indice não encontrado. Digite o indice do jogador:"))
    else:
        if time[busca]['sexo'] in 'M':
            print(f"--- LEVANTAMENTO DO JOGADOR {time[busca]['nome'].upper()}:")
        elif time[busca]['sexo'] in 'F':
            print(f"--- LEVANTAMENTO DA JOGADORA {time[busca]['nome'].upper()}:")
        for i, g in enumerate(time[busca]["gols"]):
            if g == 0:
                print(f"    No jogo {i+1} fez {g} gol.")
            elif g == 1:
                print(f"    No jogo {i+1} fez {g} gol.")
            else:
                print(f"    No jogo {i+1} fez {g} gols.")
        print("-" * 60)
    resp = input("Deseja continuar? [S/N]:").upper()[0]
    while resp not in "SsNn":
        resp = input("Resposta inválida. Deseja continuar? [S/N]:").upper()[0]
    if resp in "Nn":
        break



