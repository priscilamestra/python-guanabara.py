print("Cálculo do fatorial")

from math import factorial
n = int(input("Digite um número para calcular o fatorial dele:"))
f = factorial(n)
print("O fatorial de {} é {}." .format(n,f))

c = n
fat = 1 # fator nulo de uma multiplicação é um. diferente da soma e subt que é zero.
while c > 0: #fatorial vai até o 1
    print("{}" .format(c), end=" ")
    print("x" if c > 1 else "=", end=" ") 
    fat = fat * c 
    c = c - 1
print("{}." .format(fat))