print("Tabuada v.2")

n = int(input("Digite um número para ver sua tabuada:"))
for c in range(1,11):
    resultado = n * c 
    print("{} x {} = {}." .format(n,c,resultado))
    # ou faz a multiplicação direta dentro do format (n,c, n*c)