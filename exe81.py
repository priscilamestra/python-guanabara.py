print("Extraindo dados de uma lista")

numeros = []
while True:
    n = int(input("Digite um valor:"))
    if n not in numeros:
        numeros.append(n)
    else:
        n = int(input("Valor já digitado, digite um valor:"))
    resposta = input("Deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SsNN":
        resposta = input("Resposta inválida. Deseja continuar? [S/N]:")
    if resposta in "Nn":
        break
numeros.sort(reverse = True)
print(f"Você digitou {len(numeros)} elementos")
print(f"Os valores em ordem descrescente são {numeros}.")
if 5 in numeros:
    print(f"O valor 5 faz parte da lista")
elif 5 not in numeros:
    print(f"O valor 5 não foi encontrado na lista.")   
