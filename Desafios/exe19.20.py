# -*- coding: utf-8 -*-
from random import choice, shuffle

n1 = input("Digite o primeiro nome:")
n2 = input("Digite o segundo nome:")
n3 = input("Digite o terceiro nome:")
n4 = input("Digite o quarto nome:")

lista = [n1,n2,n3,n4]
escolhido = choice(lista)

print(f"O aluno escolhido foi {escolhido}!") 

shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)
 
