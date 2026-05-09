print("Validação de dados")

sexo = input("Informe seu sexo [M/F]:").strip().upper()[0]
#idade = int(input("Informe sua idade:"))
while sexo not in "MmFf":
    sexo = input("Dados inválidos. Por favor, informe seu sexo:").strip().upper()[0]
print(sexo)
