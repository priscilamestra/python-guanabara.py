print("função que descobre o maior")

def maior(*num):
    if len(num) > 0:
        print(f"O maior número de {num} é {max(num)}.")
    else:
        print("Nenhum número foi informado.")
        
# programa principal
while True:
    n1 = int(input("primeiro número:"))
    n2 = int(input("Segundo número:"))
    n3 = int(input("Terceiro número:"))
    maior(n1,n2,n3) 
    resp = input("Deseja continuar? [S/N]:").upper()[0]
    if resp in "nN":
        break 
