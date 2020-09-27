print("Mais sobre matrizes")

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = mai = soma_coluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor:[{l},{c}]"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
    if matriz [l][c] % 2 == 0:
        soma_par = soma_par + matriz[l][c]

print(f"A soma dos pares é {soma_par}")
for l in range(0,3):
    soma_coluna = soma_coluna + matriz[l][2]
print(f"A soma da terceira coluna é {soma_coluna}.")
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior da segunda linha é {mai}.")
