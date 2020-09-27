print("Análise de dados do grupo")

maior_idade = maior_f = maior_m = 0
while True:
    idade = int(input("Idade:"))
    sexo = input("Sexo: [F/M]").strip().upper()[0]
    while sexo not in "FfMm":
        sexo = input("Respota inválida. Sexo: [F/M]")
    resposta = input("Deseja continuar ? [S/N]:").strip().upper()[0]
    if idade >= 18:
        maior_idade = maior_idade + 1 
        if sexo in "F" and idade >= 18:
            maior_f = maior_f + 1
        elif sexo in "M" and idade >= 18:
            maior_m = maior_m + 1
    while resposta not in "SsNn":
        resposta = input("Resposta inválida. Deseja continuar ? [S/N]:").strip().upper()[0]
    if resposta == "N":
        break   
print(f"Total de pessoas com mais de 18: {maior_idade}")
if maior_f == 1 and maior_m == 1:
    print(f"Ao todo temos {maior_m} homem e {maior_f} mulher maiores de idade.")
elif maior_f == 1:
    print(f"Ao todo temos {maior_m} homens e {maior_f} mulher maiores de idade.")
elif maior_m == 1:
    print(f"Ao todo temos {maior_m} homem e {maior_f} mulheres maiores de idade.")
elif maior_f > 1 and maior_m > 1:
    print(f"Ao todo temos {maior_m} homens e {maior_f} mulheres maiores de idade.")
elif maior_f < 1 or maior_m < 1:
    print(f"Ao todo temos {maior_m} homens e {maior_f} mulheres maiores de idade.")



        



