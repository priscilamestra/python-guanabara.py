# -*- coding: utf-8 -*-
from math import trunc
print("Quebrando um número")
num = float(input("Digite um número:"))
print(f"O número {num} tem a parte inteira {num:.0f}")

num1 = float(input("Digite um número:"))
print(f"O número {num1} tem a parte inteira {trunc(num1)}")

num2 = float(input("Digite um número:"))
print(f"O número {num2} tem a parte inteira {int(num2)}")
