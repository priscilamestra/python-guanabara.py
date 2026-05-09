print("Criando um menu de opções")
from time import sleep

num1 = int(input("Digite o primeiro valor:")) # ESTUDAR TRATAMENTO DE ERRO PARA CASO O USUÁRIO DIGITE STR
num2 = int(input("Digite o segundo valor:"))
maior = 0
opção = 0 # já que o intervalo de opções está entre 1 e 5, o 0 não vai interfirir.
while opção != 5: #enquanto a opção n for 5, o programa vai reptir o menu.
    print(""" 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR""") # dentro das aspas triplas a indentação não é necessário
    opção = int(input("Escolha a sua opção:"))
    while opção < 1 or opção > 5: # validação de resposta
        opção = int(input("Opção inválida. Digite novamente:"))
    if opção == 1:
        print(num1 + num2)
    if opção == 2:
        print(num1*num2)
    if opção == 3:
        for i in range(1,2): # já que é uma operação binária* 
            if i == 1: # o primeiro do intervalo é igual a 1
                maior = num1 # por ser o primeiro, ele é o maior até o segundo num for digitado e verificado.
            if num2 > num1: # se o segundo num digitado for maior que o primeiro, ele assume a variável 'maior'.
                maior = num2
        print(maior)
    if opção == 4:
        num1 = int(input("Digite o primeiro novo número:"))
        num2 = int(input("Digite o seguno novo número:"))
    if opção == 5:
        sleep(1)
        print("Programa finalizado, volte sempre!")
        exit()

