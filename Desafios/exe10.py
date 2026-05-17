print("Conversor de moeda")
real = float(input("Valor em real: R$"))
dolar = real / 5.59
euro = real / 6.05
print(f"Com R${real:.2f} você pode comprar: U${dolar:.2f}")
print(f"Com R${real:.2f} você pode comprar: €{euro:.2f}")