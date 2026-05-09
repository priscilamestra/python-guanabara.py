print("Alistamento militar")
from datetime import date
nome = input("Nome completo:").strip().upper()
print("Escolha uma das opções:")
print("[1] - Mulher")
print("[2] - Homem")
opçao = int(input("Sua opção:"))
while opçao < 1 or opçao > 2:
    opçao = int(input("Opção inválida. Digite novamente:"))
if opçao == 1:
    print("Questionário encerrado. Obrigado(a)!") 
    exit() #encerrar o programa para essa resposta.
atual = date.today().year
nasc = int(input("Ano de nascimento:"))
#if ano == 0:
    #ano = date.today().year
idade = atual - nasc
maior = idade - 18
menor = 18 - idade
print("Quem nasceu em {} tem {} anos em {}." .format(nasc,idade,atual))
if idade == 18:
    print("Você tem que se alistar esse ano.")
elif idade > 18:
    print("Você já deveria ter se alistado há {} anos." .format(maior))
else:
    print("Ainda faltam {} anos para o alistamento." .format(menor))


