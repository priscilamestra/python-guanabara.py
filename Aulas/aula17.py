num = [2,5,5,5,9,1]
num[2] = 3 # vai substituir na posição 2, ou seja o numero 9
#num[4] = 7 # vai dar erro, eu n posso adicionar dessa maneira
num.append(7) # vai adc o numero 7
num.insert(2,0) #iserir na posição 2 o valor 0, vai jogar o numero nessa posição pra frente
num.sort() # vai colocar em ordem crescente
num.sort(reverse=True) #vai colocar em ordem decrescente 
num.pop() #vai retirar o ultimo valor
num.pop(2) #vai retirar o número nessa posição
num.remove(5) #remove procura o número do inicio da lista até o final e retira a primeira ocorrencia 
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4.")

print(f"Essa lista tem {len(num)} elementos.") #função len retorna quantos elementos tem

valores = []
valores.append(8)
valores.append(5)
for v in valores: #para cada valor em valores
    print(f"{v}...")
for c, v in enumerate(valores): #alem do valor o indice (as chaves(c)) e o valor (v), enumerate pega tanto a chave como o valor
    print(f"Na posição {c} encontrei o valor {v}.")
numeros = []
for cont in range(0,5):
    numeros.append(int(input("Digite um valor:")))
a = [2,3,4,7]
b = a #quando iguala uma lista na outra, o python liga uma ligação entre elas
b[2] = 8 #na posição 2 vai substituir o 4 pelo 8 nas duas listas
print(b)
b = a [:] #COPIA DA LISTA A, OU SEJA PEGA TDS OS VALORES DE A E JOGA EM B

