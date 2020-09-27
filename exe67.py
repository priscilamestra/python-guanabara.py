print("Tabuada V.3")

while True:
    n = int(input("Digite um número para ver sua tabuada:")) #tratamento de erro pra erro do usuário 
    if n == 0:#logo depois de verificar o número
        break
    for c in range(0,10):
        c = c + 1 #LEMBRA DO LOOPING , TEM QUE CONTAR A VARIÁVEL + 1 !!!!!!
        print(f"{n} x {c} = {n*c}")
print("TABUADA ENCERRADA, VOLTE SEMPRE!")
    #while c > 0 and c <= 10:
        #c = c + 1 #LEMBRA DO LOOPING , TEM QUE CONTAR A VARIÁVEL + 1
        #print(f"{n} x {c} = {n*c}")


