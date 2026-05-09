# -*- coding: utf-8 -*-
print("Analisando texto")

nome = input("Digite seu nome completo:").strip()
print("------- Analisando seu nome -------")
print("Seu nome em maiúsculo é {}." .format(nome.upper()))
print("Seu nome em minúsculo é {}.".format(nome.lower()))
print("Seu nome tem ao todo {} letras." .format(len(nome.replace(" ",""))))
print("Seu primeiro nome é {} e ele tem {} letras." .format(nome.split()[0],len(nome.split()[0])))
#print("Seu primeiro nome tem {} letras." .format(nome.find(" "))) 
nome1 = ("priscila mestra canto pereira")
print(nome1.find("tra")) 
print("Seu primeiro nome tem {} letras." .format(nome1.find(" "))) #find conta a posição do espaço, começa em 0.


