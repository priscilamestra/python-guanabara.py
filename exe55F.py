print("Maior e menor da sequência.")

maior = 0 #colocar 0 para se iniciar no primeiro número do intervalo
menor = 0
for i in range(1,4): # i == pessoas
    peso = float(input("Peso da {}° pessoa:" .format(i)))
    if i == 1: #o primeiro peso (primeiro num do intervalo) vai ser o maior e o menor
        maior = peso 
        menor = peso
    else: #como o else ta dentro do laço, isso vai se reptir até completar o intervalo. # else: se não for a primeira pessoa, vai entrar nas condições aninhadas
        if peso > maior: 
            maior = peso #se o segundo peso for maior que o primeiro, ele se torna o maior
        if peso < menor:
            menor = peso #se o segundo peso for manor que o primeiro, ele se torna o menor
print("Maior peso lido foi de {}kg." .format(maior)) #fora do laço para imprimir só quando tiver todos os pesos.
print("Menor peso lido foi de {}kg." .format(menor))


