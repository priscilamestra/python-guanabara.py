print("Contando vogais em tupla")

palavra = input("Digite uma palavra:"),input("Digite uma palavra:"),input("Digite uma palavra:")
for p in palavra:
    print(f"\nNa palavra {p} temos", end=" ")
    for letra in p: #cada palavra é uma lista de letras # para cada letra na palavra p
        if letra.lower() in 'aâãéeêiíõôou': #analise 
            print(letra, end=" ")



