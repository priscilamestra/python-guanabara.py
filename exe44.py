print("Gerenciador de pagamentos")
print("{:^40}".format("LOJAS MESTRA"))

valor = float(input("Preço das compras:R$"))
print("FORMAS DE PAGAMENTO:")
print("[1] á vista no dinheiro.")
print("[2] á vista no cartão de débito.")
print("[3] 2x no cartão de crédito.")
print("[4] 3x ou mais no cartão de crédito.")
opção = int(input("Qual opção?")) 
desconto1 = valor - (10 * valor / 100)
desconto2 = valor - (5 * valor / 100)
juros = valor + (20 * valor / 100)
duas_vezes = valor / 2
while opção < 1 or opção > 4:
    opção = int(input(print("Opção inválida, digite novamente:")))
if opção == 1:
    valor = desconto1
    print("Valor final = R${:.2f}." .format(desconto1))
elif opção == 2:
    valor = desconto2
    print("Valor final = R${:.2f}." .format(desconto2))
elif opção == 3:
    parcelas = valor / 2
    print("Valor final = R${} dividido em 2x com parcelas de R${} {}SEM JUROS{}." .format(valor,duas_vezes,"\033[1m","\033[m"))
else:
    vezes = int(input("Em quantas vezes?"))
    while vezes <= 2:
        vezes = int(input("Valor incorreto. Digite novamente:"))
    if vezes == 3 or vezes > 3:
        vezes = vezes
        valor = juros
        parcelas = juros / vezes  
        print("Valor final = R${:.2f} dividido em {}x com parcelas de R${:.2f} {}COM JUROS{}." .format(valor,vezes,parcelas,"\033[1m","\033[m"))
    

