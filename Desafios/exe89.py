print("Boletim com listas compostas")

ficha = []
while True:
    nome = input("Nome:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media]) #lista composta dentro da lista ficha
    resp = input("Deseja continuar? [S/N]:")
    if resp in "Nn":
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>9}')
print("-=" * 26)
for i, a in enumerate(ficha): #chave e valor dentro da lista ficha
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # aluno[nome], aluno[média] #a[1] são as notas
while True:
    notaindividual = int(input("Qual aluno você deseja ver as notas?:"))
    if notaindividual <= len(ficha) -1: #len não conta do zero, então o ultimo é n-1 #para o usuário não colocar um indice fora da lista
        print(f"Notas de {ficha[notaindividual][0]} são {ficha[notaindividual][1]}") #ficha[escolha do indice do aluno][posição referente ao nome],[posicção referente as notas do indice escolhido]
    resp = input("Deseja continuar? [S/N]:")
    if resp in "Nn":
        break
