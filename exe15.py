# -*- coding: utf-8 -*-
print("Aluguel de carros")
dias = int(input("Quanto dias alugados? "))
km = float(input("Quantods km rodados? "))
preço = (dias * 60) + (km * 0.15)

print("Preço total do aluguel: R${:.2f} " .format(preço))