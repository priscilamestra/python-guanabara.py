# -*- coding: utf-8 -*-
print("Conversor de moeda")
real = float(input("Valor em real: R$"))
dolar = real / 5.59
euro = real / 6.05
print("Com R${:.2f} você pode comprar: U${:.2f}" .format(real,dolar))
print("Com R${:.2f} você pode comprar:   {:.2f}" .format(real,euro))