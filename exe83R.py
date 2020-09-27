print("Validando expressões matemáticas")

expr = input("Digite a expressão:")
cont = []
for simb in expr: #para cada simbolo dentro da expressao
    if simb == "(": #se o simbolo for igual a "("
        cont.append("(") #vai ser adc "(" na lista cont
    elif simb == ")": #se o simbolo for igual a ")" tem dois caminhos
        if len(cont) > 0: #se o tamanho da lista for maior que 0
            cont.pop() #retira o ultimo simbolo da lista
        else:
            cont.append(")") #se o tamanho for igual a 0, adc ")" para fechar a lista
            break
if len(cont) == 0: #se o tamanho da lista for igual a 0, ou seja, a lista t vazia, os pares de "()" foram completados
    print("Sua expressão está valida.")
else:
    print("Sua expressão está errada.")
        

