print("Contagem de pares.")

for n in range(1,51): #imprimindo só números pares
    if n % 2 == 0:
        print(n, end=" ")
print("\n")    
for n in range(1,51):  #imprimindo só números ímpares
    if n % 2 != 0:
        print(n, end=" ")
print("\n")
for n in range(2,51,2): #pulando de 2 em 2 (ultimo argumento é a sequencia da contagem)
    print(n, end=" ") #número de laços é menor, ocupando menos o programa.
#criar algoritmos que exijam MENOS da máquina.