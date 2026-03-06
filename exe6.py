# -*- coding: utf-8 -*-
print("dobro, triplo e raiz quadrada")
num = int(input(" Digite um número: "))
num1 = num*2
num2 = num*3
num3 = num**(1/2)
print(f" O dobro de {num} é {num1} \n O triplo de {num} é {num2} \n A raiz quadrada de {num} é {num3:.2f}")

#sem variável

print(f" o dobro de {num} é {num*2} \n o triplo de {num} é {num*3} \n A raiz quadrada de {num} é {num**(1/2):.2f}") 

#outra forma de calcular a raiz quadrada pow(n,1/2)
print(f" A raiz quadrada de {num} é {pow(num,1/2):.2f}")
