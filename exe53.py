print("Detector de palíndromo")

frase = input("Digite uma frase:").strip().upper() #strip = ignorar os espaços antes e depois #upper = tudo em maíusculo
palavra = frase.split() #split = separa as palavras em forma de lista.(vetores)
junto = "".join(palavra) #join = junta tudo numa str só #"" = junta sem espaço
inverso = ""
for letra in range(len(junto)-1,-1,-1): #len = contador #-1 sempre que quiser de trás pra frente e pra não anular a última letra ou número.
    inverso = inverso + junto[letra]
# ou no lugar do for usar:
# inverso = junto [::-1] #fatiamento de trás pra frente.
print("O inverso de {} é {}." .format(junto,inverso))
if inverso == junto:
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")

