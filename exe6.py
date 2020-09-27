# -*- coding: utf-8 -*-
print("dobro, triplo e raiz quadrada")
num = int(input(" Digite um número: "))
num1 = num*2
num2 = num*3
num3 = num**(1/2)
print(" O dobro de {} é {}.\n O triplo de {} é {}.\n A raiz quadrada de {} é {:.2f}." .format(num, num1,num, num2, num, num3 ))

#sem variável

print(" o dobro de {} é {}.\n o triplo de {} é {}.\n A raiz quadrada de {} é {:.2f}." .format(num,(num*2),num,(num*3), num, (num**(1/2))))