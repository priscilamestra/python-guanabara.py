print("Números primos:")

n = int(input("Digite um número: "))
div = 0
for i in range (1,n + 1): #começou por 1 pra poupar o processador de retrabalho, primo / 1 e por ele mesmo.
    if n % i == 0: # número primo
        print("\033[33m", end=" ")
        div = div + 1 #total de divisões 

    else: # não primo
        print("\033[31m", end=" ")
    print( f" {i} ", end=" ") #intervalo de 1 a n+1 
if div == 1:
        print(f"\n\033[mO número {n} foi dividido {div} vez.")
else:
    print(f"\n\033[mO número {n} foi dividido {div} vezes.")
if div == 2:
    print(f"Logo, ele {('\033[1m')}é primo{('\033[m')}.")
else:
    print(f"Logo, ele {('\033[1m')}não é primo{('\033[m')}.")


# EXERCÍCIO 52 - NÚMERO PRIMO (VERSÃO 2)
# número primo só divide por 1 e por ele mesmo, totalizando sempre 2 divisões
num = int(input("Digite um número: "))

total = 0
for c in range(1, num + 1):
  if num % c == 0: 
    # 1. MOSTRA O NÚMERO EM VERMELHO (DIVISÍVEL)
    print(f'\033[33m{c}\033[m', end=' ')
    total = total + 1
  else:
    # 2. MOSTRA O NÚMERO EM AMARELO (NÃO DIVISÍVEL)
    print(f'\033[31m{c}\033[m', end=' ')

# 3. FRASE FINAL (SAIRÁ BRANCA POR CAUSA DOS RESETS ACIMA)
print(f'\033[m\nO número {num} foi dividido {total} vezes')
        
    