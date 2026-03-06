# -*- coding: utf-8 -*-
print ("média dos alunos retardados! ")
nota1 = float(input("Digite sua primeira nota bosta:"))
#nota1 = float(nota1)
nota2 = float(input("Digite sua segunda nota: "))
#nota2 = float(nota2)
media = (nota1 + nota2) / 2

if (nota1 + nota2) /2 >= 60:
    print(f"Média: {media:.2f} \nParabéns, você não fez mais que sua obrigação!")
else:
    print(f"Média: {media:.2f} \nReprovado, você é idiota? ")

input()










