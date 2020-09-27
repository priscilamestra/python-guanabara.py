# -*- coding: utf-8 -*-
print("Quebrando um número")
num = float(input("Digite um número:"))
print("O número {} tem a parte inteira {:.0f}" .format(num,num))

from math import trunc
num1 = float(input("Digite um número:"))
print("O número {} tem a parte inteira {}" .format(num1,trunc(num1)))

num2 = float(input("Digite um número:"))
print("O número {} tem a parte inteira {}" .format(num2, int(num2)))

