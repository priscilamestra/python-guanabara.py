print("Função de contador")
from time import sleep

def contador(i, f, p): # inicio, fim, passo é a msg que vai ser exibida para o usuário
    if p < 0: #passo tem que ser positivo
        p *= -1
    if p == 0: #passo igual a zero não existe
        p = 1
    print(f"\nContagem de {i} até {f} de {p} em {p}.\n") #estrutura da função
    if i < f:
        cont = i
        while cont <= f:
            print(f" {cont}", end='', flush = True) #flush = True é para não dar bug no sleep
            sleep(0.5)
            cont += p # cada passo vai contar
    if i > f:
        cont = i
        while cont >= f:
            print(f" {cont}", end='', flush = True)
            sleep(0.5)
            cont -= p # para cada passo a menos ele vai contar

# programa principal
contador(1,10,1) #contador é a chamada da funç, e os paramentos dentro dos () passarão no lugar dos parametros da estrutura
contador(10,0,2)
print("\nAgora é a sua vez de personalizar a contagem")
ini = int(input("Início:"))
fi = int(input("Fim:"))
pas = int(input("Passo:"))
contador(ini,fi,pas)