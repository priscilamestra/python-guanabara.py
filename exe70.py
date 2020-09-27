print("Estatísticas em produtos")
print("BARATÃO DA SERRA")
print("Desconto de 15% em compras acima de R$ 500,00.")

soma = menor = maior = cont = descont = 0
prod_maior = prod_menor = " " # " " isso é: não tem prod mais caro e mais barato ainda
while True:
    produto = input("Nome do produto:").strip().upper()
    preço = float(input("Preço: R$"))
    cont = cont + 1
    quantidade = int(input("Quantidade:"))
    soma = soma + (quantidade*preço)
    while quantidade < 1:
        quantidade = int(input("Valor inválido. Quantidade:"))
    resposta = input("Deseja continuar ? [S/N]:").strip().upper()[0]
    if soma > 500:
        descont = (15 * soma) / 100
        soma = soma - descont
    if cont == 1:
        menor = preço
        prod_menor = produto
        maior = preço
        prod_maior = produto
    elif cont != 1:     
        if preço < menor:
            menor = preço
            prod_menor = produto
        else:
            maior = preço
            prod_maior = produto
    while resposta not in "SN":
        resposta = input("Resposta inválida. Deseja continuar ? [S/N]:").strip().upper()[0]
    if resposta in "N":
        break
print(f"Total das compras :R${soma}")
print(f"Produto com menor preço: {prod_menor}  custando R${menor:.2f}.")
print(f"Produto com maior preço: {prod_maior} custando R${maior:.2f}.")
