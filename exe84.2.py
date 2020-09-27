print("Lista composta e análise de dados")

temp = []
princ = []
mai = men = 0
while True:
    temp.append(input("Digite um nome:"))
    temp.append(float(input("Peso (kg):")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) 
    temp.clear()    
    resposta = input("Deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar? [S/N]:")
    if resposta in "Nn":
        break
print(f"Ao todo você cadastrou {len(princ)} pessoas.")
print(f"O maior peso cadastrado foi de {mai}kg ", end="")
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end="")
print()
print(f"O menor peso cadastrado foi {men}kg ", end="")
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end="")
