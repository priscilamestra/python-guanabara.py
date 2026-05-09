print("Vários números com flag")

soma = cont = 0
while True:
    n = int(input("Digite um número:"))
    if n == 0: # eu verifico se o número é 0 antes de somar e contar
        break
    cont = cont + 1 # só vai considerar cont e soma se não for 0 #se colocar em cima do if o flag vai ser contado
    soma = soma + n
print(f"Você digitou {cont} e a soma é {soma}.") # Fstrings ex : (f"{salário:.2f}.")



