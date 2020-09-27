print("Maiores e Menores valores.")

cont = soma = maior = menor = 0
resposta = "S"
while resposta in "Ss":
    n = int(input("Digite um número:"))
    resposta = input("Deseja continuar? [S/N]:").strip().upper()
    cont = cont + 1 #tem que ficar perto da variável de comando, pra contar e somar após a resposta [S/N]
    soma = soma + n #""
    if cont == 1: #cont = 1 (primeiro número digitado)
        maior = menor = n # o primeiro é sempre maior e menor
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar? [S/N]:").strip().upper()
media = soma / cont
print("Você digitou {} números e a média dele é {:.2f}." .format(cont,media))
print("O maior número digitado é {} e o menor é {}." .format(maior,menor))

