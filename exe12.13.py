# -*- coding: utf-8 -*-
print("Calculando descontos")
preço = float(input("Qual é o preço do produto? R$"))
desconto = int(input("Qual a porcentagem de desconto?"))
conta = desconto*preço/100
preçofinal = preço - conta

print(f"O produto que custava R${preço:.2f}, na promoção com desconto de {desconto}% vai custar R${preçofinal:.2f}.")

print("Reajuste do funcionário")
salário = float(input("Qual salário do funcionário? R$"))
porcentgem = int(input("Qual é a porcentagem?"))
conta2 = porcentgem*salário/100
salário2 = salário + conta2

print(f"Um funcionário que ganhava R${salário:.2f}, com {porcentgem}% de aumento, passa a receber R${salário2:.2f}.")