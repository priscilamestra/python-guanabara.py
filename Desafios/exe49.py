print("Tabuada v.2")

n = int(input("Digite um número para ver sua tabuada: "))
for c in range(1,11):
    resultado = n * c 
    print(f"{n} x {c:2} = {resultado}")
    # ou faz a multiplicação direta dentro do format (n,c, n*c)

# outro jeito de fazer a tabuada, usando um contador para o multiplicador:
tab = input("Digite um número para ver sua tabuada: ")
tab = int(tab)
cont = 0
for c in range(1,11): # c igual contador que vai de 1 a 10
  cont = cont + 1
  print(f"{tab} x {cont:2} = {tab * cont}")
