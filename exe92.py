from datetime import datetime

cad = {}
cad['nome']= input("Nome:")
nasc = int(input("Ano de nascimento:"))
cad['idade'] = datetime.now().year - nasc
cad['CTPS'] = int(input("N° da CTPS (0 caso não tenha):"))
if cad['CTPS'] != 0:
    cad['ano da contratação'] = int(input("Ano de contratação:"))
    cad['salário'] = float(input("Salário: R$"))
    cad['aposentadoria'] = cad['idade'] + ((cad['ano da contratação'] + 35) - datetime.now().year)  # considerando 35 anos de contribuição 
print("-=" * 26)
for k, v in cad.items():
    print(f"{k} = {v}")