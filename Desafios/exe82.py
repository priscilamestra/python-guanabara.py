print("Dividindo valores em várias listas")
tudo = []
par = []
impar = []
while True:
    n = int(input("Digite um valor:"))
    tudo.append(n)
    if n != 0:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    resposta = input("Deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar? [S/N]:")
    if resposta in "Nn":
        break
tudo.sort()
par.sort()
impar.sort()    
print(f"A lista completa é: {tudo}")
print(f"A lista de pares é: {par}")
print(f"A lista de impares é: {impar}")
