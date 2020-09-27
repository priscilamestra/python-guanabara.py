# -*- coding: utf-8 -*-
print("Primeiro e último nome da pessoa.")

nome = input("Digite seu nome completo:").strip().upper()
apelido = input("Como você gostaria de ser chamado ? ").strip().upper()
print("Muito prazer em te conhecer,{}!" .format(apelido))
print("Seu primeiro nome é {}." .format(nome.split()[0]))
print("Seu último nome é {}." .format(nome.split(" ")[-1]))  # -1 pra acertar a posição 0 split espaço pra contar direita pra esquerda

