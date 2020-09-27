print("Funções parte 1")

def lin(): #definição da função
    print("-" * 30)

# programa principal
lin()
print("  MESTRA PRODUÇÕES  ")  
lin()
print("  DESENVOLVEDORA PYTHON  ")  
lin()

def titulo(txt):
    print("-" * 30)
    print(txt) #parametro não precisa de ""

titulo('PYTHON DEVELOPER')

def soma(a, b): #soma vai receber dois números
    s = a + b
    print(s)

#programa principal    
soma(5, 2)
soma(8, 9)    

def contador(* num):
    tam = len(num) #tamanho de num
    print(tam)

contador(1,2,3)
contador(5,9,11)
contador(2,4,6,8)    

def cont(*num):
    for valor in num:
        print(f"{valor} ", end ="")
        

cont(7,8,9)
cont(4,5,6)
print()

def dobra(lista):
    pos = 0 #posição zero
    while pos < len(lista):
        lista[pos] *= 2 #lista[pos] = lista[pos] * 2
        pos += 1 #para não travar a máquina.

valores= [6,3,9,1,0,2]
dobra(valores)
print(valores)        

def soma(* valores): # *Empacotar parametros
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}.")

soma(5,2)
soma(2,9,4)   