print("Analisando empréstimo")

casa = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))
prestação = casa / (12 * anos)
minimo = 30 * salário / 100

print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}" .format(casa,anos,prestação))
if prestação <= minimo:
    print("Empréstimo \033[1;32maprovado\033[m.")
else:
    print("Empréstimo \033[1;31mrecusado\033[m.")