print("Maior e menor da sequência.")

maior = 0 #colocar 0 para se iniciar no primeiro número do intervalo
menor = 0
for i in range(1,4): # i == pessoas
    peso = float(input(f"Peso da {i}° pessoa: "))
    if i == 1: #o primeiro peso (primeiro num do intervalo) vai ser o maior e o menor
        maior = peso 
        menor = peso
    else: #como o else ta dentro do laço, isso vai se reptir até completar o intervalo. # else: se não for a primeira pessoa, vai entrar nas condições aninhadas
        if peso > maior: 
            maior = peso #se o segundo peso for maior que o primeiro, ele se torna o maior
        if peso < menor:
            menor = peso #se o segundo peso for manor que o primeiro, ele se torna o menor
print(f"Maior peso lido foi de {maior}kg.") #fora do laço para imprimir só quando tiver todos os pesos.
print(f"Menor peso lido foi de {menor}kg.")


# EXERCÍCIO 55 - Maior e menor da sequência (VERSÃO 2)

maior_peso = 0
menor_peso = 0

for pessoa in range(1, 4):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
    
    # PASSO 1: A INAUGURAÇÃO (Tratando a primeira pessoa)
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    
    # PASSO 2: A COMPETIÇÃO (Para as outras pessoas)
    else:
        # Verifica se o novo peso ganha o troféu de MAIOR
        if peso > maior_peso:
            maior_peso = peso
        
        # Verifica se o novo peso ganha o troféu de MENOR
        elif peso < menor_peso:
            menor_peso = peso

print(f"O maior peso lido foi {maior_peso}kg")
print(f"O menor peso lido foi {menor_peso}kg")