print("IMC")

kg = float(input("Qual é o seu peso? (Kg):"))
altura = float(input("Qual é a sua altura? (m):"))
print("Escolha uma das opções:")
print("[1] - Mulher")
print("[2] - Homem")
opçao = int(input("Sua opção:"))
while opçao < 1 or opçao > 2:
    opçao = int(input("Opção inválida. Digite novamente:"))
if opçao == 1:
    imc = kg / (altura ** 2)  
elif opçao == 2:
    imc = kg / (altura ** 2) 
#imc = kg / (altura ** 2) #colocar lógica para calcular imc para mulheres.
print("Seu IMC é {:.1f} " .format(imc), end="")
if imc < 18.5:
    print("\033[31mAbaixo do peso\033[m.")
elif imc >= 18.5 and imc < 25:
    print("\033[32mPeso ideal\033[m.")
elif imc > 25:
    print("\033[32mSobrepeso\033[m.")
elif imc <= 30 and imc < 40:
    print("\033[34mObesidade\033[m.")
else:
    print("\033[33mObesidade Mórbida\033[m.")    
