print("unindo dicionários e listas")

dados = {}
pessoas = []
soma = media = 0
#validação dos dados 
while True:
    dados.clear()
    dados['nome'] = input("Nome:")
    dados['sexo'] = input("Sexo [F/M]:").upper()[0]
    while dados['sexo'] not in "FM": #pode ser usado o while True para cada validação
        dados['sexo'] = input("Resposta inválida. Sexo [F/M]:").upper()[0]
    dados['idade'] = int(input("Idade:"))
    soma = soma + dados['idade']
    pessoas.append(dados.copy())
    resp = input("Deseja continuar ? [S/N]:").upper()[0]
    while resp not in "SN":
        resp = input("Resposta inválida. Deseja continuar ? [S/N]:").upper().strip()
    if resp in "Nn":
        break
#analise dos dados    
media = soma / len(pessoas)    
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas.')
print(f"A média das idades é {media:5.2f} anos.")
print(f'As mulheres cadastradas foram: ', end="")
for p in pessoas:
    if p['sexo'] in "fF":
        print(f"{p['nome']} ", end="")
print()
print("Lista das pessoas que estão acima da média: ", end='')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print() 