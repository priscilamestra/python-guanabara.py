# -*- coding: utf-8 -*-
print("Calculando descontos")
preço = float(input("Qual é o preço do produto? R$"))
desconto = int(input("Qual a porcentagem de desconto?"))
conta = desconto*preço/100
preço1 = preço - conta

print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}." .format(preço,desconto,preço1))

print("Reajusto do funcionário")
salário = float(input("Qual salário do funcionário? R$"))
porcentgem = int(input("Qual é a porcentagem?"))
conta2 = porcentgem*salário/100
salário2 = salário + conta2

print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}." .format(salário,porcentgem,salário2))