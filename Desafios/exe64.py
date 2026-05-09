print("Tratando vários valores V.1")
from time import sleep

n = cont = soma = 0
n = int(input("Digite um número [0 para parar]:")) #como se fosse um primeiro programa e como não tem comando nenhum ele segue pra próxima linha do código que entra no laço
sleep(1) #coloquei o sleep pra mostrar que segunda vez que você digita já entrou no laço ou seja, não vai demorar 1s pra responder
while n != 0:
    #n = int(input("..."))
    #if n != 0: 
        #cont = cont + 1
        #soma = soma + 1
    cont = cont + 1 
    soma = soma + n
    n = int(input("Digite um número [0 para parar]:"))
print("Você digitou {} números e a soma dele é {}." .format(cont,soma))
# se digitar no primeiro comando 999, ele n vai contar e somar nada, pq o cont e soma só funcionam dentro do laço
# e o print mostra só o cont e soma.
        
    


