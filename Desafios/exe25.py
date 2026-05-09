# -*- coding: utf-8 -*-
print("Procurando uma string dentro de outra.")

nome = input("Qual seu nome completo? ").strip()
print("Seu nome tem silva? {}" .format("SILVA" in nome.upper().split())) 

curso = input("Qual seu curso? ").strip()
print("Você cursa alguma engenharia? {}" .format("ENGENHARIA" in curso.upper().split()))


email = input("Qual seu email? ").strip()
print(email.lower()) #caso o usuário coloque em maiúsculo ou com espaço 


