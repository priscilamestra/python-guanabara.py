print("listas com pares e ímpares")

num = [[], []] # lista de indice [0] e lista de indice [1] dentro da lista num
valor = 0
for n in range(1,5):
    valor = int(input(f"Digite o {n}° valor:"))
    if not valor == 0: #para não contar o zero
        if valor % 2 == 0:
            num[0].append(valor) #[0] é referente a lista de indice 0 dentro lista num
        else:
            num[1].append(valor)
num[0].sort() #vai organizar cada lista de forma independente 
num[1].sort()
print(f"Todos os valores:{num}")
print(f"Os valores pares digitados foram:{num[0]}")
print(f"Os valores ímpares digitados foram:{num[1]}")

