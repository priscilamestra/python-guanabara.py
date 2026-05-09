print("Lista composta e análise de dados")

dados = []
while True:
    nome = (input("Digite um nome:"))
    peso = (float(input("Peso (kg):")))
    dados.append([nome, peso]) #desse modo fica com 2 argumentos
    resposta = input("Deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar? [S/N]:")
    if resposta in "Nn":
        break
#list comprehension



print(f"Ao todo você cadastrou {len(dados)} pessoas.")
maior_peso = max([p for n, p in dados])
print(f"O maior peso cadastrado foi de {maior_peso:.1f}kg ", end="")
print(f'{[n for n, p in dados if p == maior_peso]}')
menor_peso = min([p for n, p in dados])
print(f"O menor peso cadastrado foi {menor_peso:.1f}kg ", end="")
print(f'{[n for n, p in dados if p == menor_peso]}')


#print(max(dados)) 
#print(min(dados))
