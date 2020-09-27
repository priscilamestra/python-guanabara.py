print("5 valores numéricos")

valores = []
for cont in range(0,5):
    valores.append(int(input(f"Digite um valor na posição {cont}:")))
print(f"Você digitou os números: {valores}.")
for p, v in enumerate(valores):
    if v == max(valores):
        print(f"Maior valor digitado é {max(valores)} e sua posição é {p}.")
    if v == min(valores):
        print(f"Menor valor digitado é {min(valores)} e sua posição é {p}.")

lista_teste = []
mai = men = 0
for c in range (0,3):
    lista_teste.append(int(input(f"Digite um valor na posição {c}:")))
    if c == 0:
        mai = men = lista_teste[c]
    else:
        if lista_teste[c] > mai:
            mai = lista_teste[c]
        if lista_teste[c] < men:
            men = lista_teste 
print(f"Maior número digitado na lista teste é {mai}.")
print(f"Menor número digitado na lista teste é {men}")

    
