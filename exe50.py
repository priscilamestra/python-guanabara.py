print("Soma dos pares.")
soma = 0
cont = 0
for c in range(1,7): # c vai ser a variável no intervalo de 1 a 6. 
    n = int(input("Digite um número:"))
    if n % 2 == 0: #se n for divisível por 2 ...
        soma = soma + n # vai somar só o que foi pedido no if ( está dentro da identação)
        cont = cont + 1 # vai contar só o que foi pedido no if ( está dentro da identação)
if cont == 1 or cont == 0:
    print("Você informou {} número PAR e a soma dos números pares é {}." .format(cont,soma))
else:
    print("Você informou {} números PARES e a soma dos números pares é {}." .format(cont,soma)) #print nesse caso tem que ficar do lado de fora senão ele vai entrar no laço assim que cumprir o que foi comandado.
        

