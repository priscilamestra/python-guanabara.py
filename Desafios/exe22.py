print("Analisando texto")

nome = input("Digite seu nome completo:").strip()
print("------- Analisando seu nome -------")
print(f"Seu nome em maiúsculo é {nome.upper()}.")
print(f"Seu nome em minúsculo é {nome.lower()}.")
print(f"Seu nome tem ao todo {nome.replace(" ", "")} letras.")
print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split([0]))} letras.")
#print("Seu primeiro nome tem {} letras." .format(nome.find(" "))) 
nome1 = ("priscila mestra canto pereira")
print(nome1.find("tra")) 
print(f"Seu primeiro nome tem {nome1.find(" ")} letras.") #find conta a posição do espaço, começa em 0.


