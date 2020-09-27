print("Caixa eletrônico")
print("Cédulas de R$50,00 R$10,00 R$20,00 e R$5,00.")
from datetime import datetime

soma = 0
while True:
    saque = int(input("Que valor você quer sacar? R$"))
    soma = soma + saque #se colocar lá embaixo, provavelmente vai se associar a uma condição aninhada.
    print("""
    [1] NOVO SAQUE
    [2] SAIR""")
    opção = int(input("\nDigite sua opção:"))
    while opção > 2 or opção < 1:
        opção = int(input("Opção inválida. Digite sua opção:"))
    if opção == 2: #while not in opção == 2
        print(f"O valor total do saque foi de R${soma}.")
        break
total = soma
ced = 50 #maior valor 
total_ced = 0 #total de cédulas de cada valor    
while True:
    if total >= ced:
        total = total - ced 
        total_ced = total_ced + 1
    else:
        if total_ced > 0 and total_ced == 1: 
            print(f"Total de {total_ced} cédula de R${ced}.")
        elif total_ced > 0:
            print(f"Total de {total_ced} cédulas de R${ced}.")
        elif ced == 50: #pesquisar o motivo de ter que colocar ced igual a 50
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        total_ced = 0 #se não colocar vai dar erro
        if total == 0:
            break
now = datetime.now()
print(now)
"""now = datetime.now()
atual = now.strftime("%H:%:M")
if now >= "13":
    print("Boa tarde")
if now <= "13":
    print("Bom dia")
if now >= "18" and now <= "6":
    print("Boa noite")"""
print("Volte sempre ao banco Mestra.") #refazer com o bom dia,tarde e noite de acordo com o horário de acesso do cliente.
