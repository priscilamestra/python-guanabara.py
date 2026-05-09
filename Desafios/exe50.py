print("Soma dos pares.")
soma = 0
cont = 0
for c in range(1,7): # c vai ser a variável no intervalo de 1 a 6. 
    n = int(input("Digite um número:"))
    if n % 2 == 0: #se n for divisível por 2 ...
        soma = soma + n # vai somar só o que foi pedido no if ( está dentro da identação)
        cont = cont + 1 # vai contar só o que foi pedido no if ( está dentro da identação)
if cont == 1:
    print(f"Você informou {cont} número PAR, logo a soma é {soma}.")
elif cont == 0:
    print("Você não informou nenhum número PAR.")
else:
    print(f"Você informou {cont} números PARES e a soma dos números pares é {soma}.") #print nesse caso tem que ficar do lado de fora senão ele vai entrar no laço assim que cumprir o que foi comandado.
        
#outra forma de fazer o mesmo exercício, usando o continue para pular os números ímpares:
print("Soma dos pares.")
soma = 0
cont = 0
for c in range(1,7):
  num = int(input(f'Digite o {c}° valor: '))
  if num % 2 == 0:
    cont = cont + 1 
    soma = soma + num
  else:
    continue
print(f'Você informou {cont} números PARES e a soma deles é {soma}')