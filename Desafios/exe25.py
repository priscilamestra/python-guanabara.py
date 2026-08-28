print("Procurando uma string dentro de outra.")

nome = input("Qual seu nome completo? ").strip()
print(f"Seu nome tem silva? {"SILVA" in nome.upper().split()}")

curso = input("Qual seu curso? ").strip()
print(f"Você cursa alguma engenharia? {"ENGENHARIA" in curso.upper().split()}")


email = input("Qual seu email? ").strip()
print(email.lower()) #caso o usuário coloque em maiúsculo ou com espaço 


