print("Validando expressão matemática")

expr = input('Digite a expressão: ')
if exp.count('(') == exp.count(')'): # count() quantas vezes aparece o que está dentro dos parenteses
    print('Sua expressão é válida!!') # se a quantidade de "(" for igual a ")" a expressao é valida
else:
    print('Sua expressão não é válida')
