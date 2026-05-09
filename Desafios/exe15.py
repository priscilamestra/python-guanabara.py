# -*- coding: utf-8 -*-
print("Aluguel de carros")
dias = int(input("Quanto dias alugados? "))
km = float(input("Quantos km rodados? "))
preço = (dias * 60) + (km * 0.15)

print(f"Preço total do aluguel: R${preço:.2f}")