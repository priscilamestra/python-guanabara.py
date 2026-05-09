print("Super progressão aritmética V.3")

primeiro = int(input("Primeiro termo:"))
razão = int(input("Razão da PA:"))
termo = primeiro
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}" .format(termo), end=" ") # end = " " joga tudo numa linha horizontal 
        termo = termo + razão 
        cont = cont + 1 # vai contar do 1 até o total
    print("\n")
    mais = int(input("Quantos termos você querm mostrar a mais?:"))
print("Progressão finalizada com {} termos analisados." .format(total)) 