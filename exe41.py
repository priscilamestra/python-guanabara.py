print("Classificando atletas")
from datetime import date

ano = int(input("Data de nascimento:"))
atual = date.today().year
idade = atual - ano
print("Escolha uma das opções:")
print("[1] - Mulher")
print("[2] - Homem")
opçao = int(input("Sua opção:"))
while opçao < 1 or opçao > 2:
    opçao = int(input("Opção inválida. Digite novamente:"))
if opçao == 1:
    print("A atleta tem {} anos." .format(idade))  
elif opçao == 2:
    print("O atleta tem {} anos." .format(idade)) 
if idade <= 9:
    print("\033[1mCLASSIFICAÇÃO\033[m: Mirim")
elif idade > 9 and idade <= 14: #pode colocar só "idade <= 14", primeiro if já retira o resto.
    print("\033[1mCLASSIFICAÇÃO\033[m: Infantil")
elif idade > 14 and idade <= 19: 
    print("\033[1mCLASSIFICAÇÃO\033[m: Junior")
elif idade > 19 and idade <= 25:
    print("\033[1mCLASSIFICAÇÃO\033[m: Sênior")
else:
    print("\033[1mCLASSIFICAÇÃO\033[m: Master")

