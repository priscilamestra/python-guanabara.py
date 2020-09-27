# -*- coding: utf-8 -*-
nome = input("Digite seu nome: ")
print("Bem vindo ao seu primeiro programa de interação,", nome + "!") 
n1 = int(input("Digite um número:" ))
n2 = int(input("Digite outro número:" ))

soma = n1 + n2
print("A soma entre", n1, "e", n2 ,"é", soma)

n3 = int(input("Digite um número:"))
n4 = int(input("Digite outro número:"))

soma2 = n3 + n4
print("A soma entre {} e {} é {}" .format(n3, n4, soma2)) 

coisa = input("Digite qqr coisa idiota: ")
print(" o tipo dessa variável é ", type(coisa))
print("tem espaço ?", coisa.isspace())
print("é inteiro? ", coisa.isalpha())
print(" é alfanumérico ?", coisa.isalnum())
print("é decimal ?", coisa.isdecimal())
print("é maiúsculo?", coisa.islower())






