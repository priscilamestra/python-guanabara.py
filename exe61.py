print("Progressão aritmética V.2")

primeiro = int(input("Primeiro termo:"))
razão = int(input("Razão da PA:"))
termo = primeiro
cont = 1 
while cont <= 10: # até o contador chegar a 10
    print("{}" .format(termo), end=" ")
    termo = termo + razão 
    cont = cont + 1 # vai contar do 1 até o 10
    
