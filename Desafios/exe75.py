print("Análise de dados em uma tupla")

num = int(input("Digite o primeiro número:")),int(input("Digite o primeiro número:")),int(input("Digite o primeiro número:")),int(input("Digite o primeiro número:"))
tupla = num #não precisa dessa variável, funciona com num
print(f"Você digitou os valores:{tupla}")
if tupla.count(9) == 1:
    print(f"O valor 9 apareceu 1 vez.")
else:
    print(f"O valor 9 apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O valor 3 apareceu na {tupla.index(3)+1}° posição.")
else:
    print("O valor 3 não foi digitado.")
print(f'Os valores pares digitados foram:' ,end = " ") #melhorar a visualização dos números pares
for n in tupla: #para cada valor n na tupla
    if n % 2 == 0: # se n % 2 for igual a zero é par
        print(n, end = " ")  
