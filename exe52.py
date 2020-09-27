print("Números primos.")

n = int(input("Digite um número:"))
div = 0
for i in range (1,n + 1): #começou por 1 pra poupar o processador de retrabalho, primo / 1 e por ele mesmo.
    if n % i == 0: # número primo
        print("\033[33m", end=" ")
        div = div + 1 #total de divisões 

    else: # não primo
        print("\033[31m", end=" ")
    print( " {} " .format(i), end=" ") #intervalo de 1 a n+1 
if div == 1:
        print("\n\033[mO número {} é dividido {} vez." .format(n,div))
else:
    print("\n\033[mO número {} é dividido {} vezes." .format(n,div))
if div == 2:
    print("Logo, ele {}é primo{}." .format("\033[1m","\033[m"))
else:
    print("Logo, ele {}não é primo{}." .format("\033[1m","\033[m"))
        
    