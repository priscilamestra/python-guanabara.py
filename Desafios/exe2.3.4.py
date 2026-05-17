# -*- coding: utf-8 -*-
nome = input("Digite seu nome: ")
print(f"Bem vindo ao seu primeiro programa de interação, {nome}!") 
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
print("A soma entre", n1, "e", n2 ,"é", soma)

n3 = int(input("Digite um número: "))
n4 = int(input("Digite outro número: "))

soma2 = n3 + n4
print(f"A soma entre {n3} e {n4} é {soma2}") 

coisa = input("Digite qqr coisa idiota: ")
print("o tipo dessa variável é ", type(coisa)) #a função type mostra o tipo da variável // print (type("qualquer coisa")) mostra o tipo da string
print("só tem espaço vazio?", coisa.isspace())
print("é um número?", coisa.isnumeric())
print("é inteiro? ", coisa.isdigit())
print("é alfabético?", coisa.isalpha())
print("é alfanumérico?", coisa.isalnum())
print("é decimal?", coisa.isdecimal())
print("é maiúsculo?", coisa.isupper())
print("é minúsculo?", coisa.islower())







