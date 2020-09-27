print("Matriz em python")

#inserir um modo que o usuário tenha como escolher sua matriz

matriz = [[0,0,0], [0,0,0], [0,0,0]] #zero para não precisar colocar o append
for l in range(0,3): #for de alimentação
    for c in range(0,3): 
        matriz[l][c] = int(input(f"Digite um valor [{l},{c}]:"))
for l in range(0,3): #for de organizar como vai ser mostrado
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=' ') #:^5 para contar 5 espaços centralizados
    print() #toda vez que ele terminar as colunas ele quebra a linha