# -*- coding: utf-8 -*-
print("Separando dígitos de um número")

num = int(input("Informe um número:"))
print("------- Analisando o número" , num, "-------")

#print("Unidade:{}" .format(n[3]))
#print("Dezena:{}" .format(n[2]))
#print("Centena:{}" .format(n[1]))
#print("Milhar:{}" .format(n[0]))  

u = num // 1 % 10  
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Unidade:", u)
print("Dezena:", d)
print("Centena:", c)
print("Milhar:", m) 