

distancia = float(input("Qual é a distância da viagem em km?"))
preço = distancia * 0.50
preço2 = distancia * 0.45

if distancia >= 200:
    print("O preço da sua passagem será R${:.2f}." .format(preço2))
else:
    print("O preço da sua passagem será R${:.2f}." .format(preço)) 