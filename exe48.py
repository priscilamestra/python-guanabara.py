print("Somando ímpares múltiplos de 3")
soma = 0
cont = 0
for n in range(1,501,2):
    if n % 3 == 0:
        cont = cont + 1 #contador conta + 1 (toda vez que o if encontrar um divisor por 3 ele vai somar +1)
        soma = soma + n #acumulador vai acumulando os valores: somando/multiplicando/dividindo,subtraindo ou seja, normalmente soma um valor.
print("A soma de todos os {} valores solicitados é de {}" .format(cont,soma))

# soma += n
# cont += 1