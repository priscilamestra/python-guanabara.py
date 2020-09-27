salario = float(input("Qual é o salário do funcionário ? R$"))
calculo1 = ((salario * 10) / 100) + salario
calculo2 = ((salario * 15) / 100) + salario

if salario > 1250:
    print("Com o reajuste, o salário de {} passará a ser R$:{:.2f} " .format(salario,calculo1))
if salario <= 1250:
    print("Com o reajuste, o salário de {} passará a ser R$:{:.2f}" .format(salario,calculo2))


#TA DANDO ERRO ESSE CARALHO AQUI EMBAIXO
#if salario <= 1250:
    #novo = salario + ((salario * 15) / 100)
#else:
    #novo = ((salario * 10) / 100) + salario
#print("Novo salário R${}." .format(salario,novo))
