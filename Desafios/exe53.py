print("Detector de palíndromo")

frase = input("Digite uma frase:").strip().upper() #strip = ignorar os espaços antes e depois #upper = tudo em maíusculo
palavra = frase.split() #split = separa as palavras em forma de lista.(vetores)
junto = "".join(palavra) #join = junta tudo numa str só #"" = junta sem espaço
inverso = ""
for letra in range(len(junto)-1,-1,-1): #len = contador #-1 sempre que quiser de trás pra frente e pra não anular a última letra ou número.
    inverso = inverso + junto[letra]
# ou no lugar do for usar:
# inverso = junto [::-1] #fatiamento de trás pra frente.
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")
   

# EXERCÍCIO 53 - Detector de palíndromo (VERSÃO 3 SEM O LOOP FOR)

frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace(' ','')
if frase != frase[::-1]:
  print("Não é um palíndromo")
else:
  print("É um palíndromo")

# EXERCÍCIO 53 - Detector de palíndromo (VERSÃO 4)

frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace(' ','')
inverso = ''

for letra in range(len(frase) - 1, -1, -1):
  inverso = inverso + frase[letra]
print(f'O inverso de {frase} é {inverso}')
if inverso == frase:
  print('Temos um PALÍNDROMO!')
else:
  print('A frase digitada não é um palíndromo!')
