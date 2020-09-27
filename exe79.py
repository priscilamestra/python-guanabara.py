print("Valores únicos em uma lista")

numeros = []
while True:
    n = int(input("Digite um número:"))
    if n not in numeros: # se o n não estiver em numeros, eu adiciono ele na lista
        numeros.append(n)
        print("Número adicionado com sucesso.")
    else:
        print("Esse número já foi digitado.")
    #numeros.sort() #ordenar do menor para o maior
    resposta = input("Deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar ? [S/N]:")
    if resposta in "Nn":
        break
numeros.sort() #ordenar do menor para o maior
print(f"Você digitou os valores: {numeros}") 

