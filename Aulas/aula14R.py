print("Aula 14")

from time import sleep 

for i in range(0,11): #sabendo o limite, dá para usar o for.
    print(i, end=" ")
print("\n") 
sleep(1)
#ou
i = 0
while i <= 10:#sabendo o limite ou não, dá para usar o while(enquanto).
    print(i, end=" ") # vai imprimir o i inicial (escolhido) para depois somar o i com +1 # end=" " para imprimir a seq na horiz.
    i = i + 1

print("\n")
n = 1 #gambiarra 
while n != 0: #flag : ponto/condição de parada
    n = int(input("Digite um número:"))

resposta = "S" 
while resposta == "S": #or resposta != str
    n = int(input("Digite um número: "))
    #while n not in int:
        #n = int(input("Resposta inválida. Digite um número inteiro:"))
    #if resposta == str: #tratamento de erro
        #n = int(input("Resposta inválida. Digite um número inteiro:"))
    resposta = input("Quer continuar? [S/N]: ").strip().upper() #se digitar n para o laço pq o mesmo só tá programado para reptir caso a resposta seja s  
    # strip para ignorar os espaços extras e upper para deixar a respota em caixa alta
    while resposta not in "SsNn":
        resposta = resposta = input("Resposta inválida. Quer continuar? [S/N]:").strip().upper()
    if resposta in "Nn":
        exit()
    
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor:"))
    if n != 0: #assim o número zero não será analisado
        if n % 2 == 0:
            par = par + 1 # vai mostrar quantos numeros pares foram digitados
        else:
            impar = impar + 1
if par == 0:
    print("Você digitou nenhum número par.")
if par == 1:
    print("Você digitou 1 número par.")
if impar == 1:
    print("Você digitou 1 número ímpar.")
if impar == 0:
    print("você digitou nenhum número ímpar.")
if par > 1:
    print("Você digitou {} números pares." .format(par))
if impar > 1:
    print("Você digitou {} números ímpares." .format(impar))
# tentar tirar um pouco dos if 










