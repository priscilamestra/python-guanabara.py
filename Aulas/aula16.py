print("TUPLAS") #tuplas são imutáveis 
#Tuplas ()
#lista []
#dicionário {}

lanche = "hamburguer", "suco", "pizza", "pudim"
for comida in lanche: #para cada comida em lanche 
    print(comida)
print(lanche)
print(len(lanche)) #[ é só quando vai referenciar o indice]
#[1:] vai do suco até o pudim
#[] para referenciar igual no fatiamento
# -1 = pudim, -2 = pizza, -3 = suco, -4 = hamburguer
#no fatiamento o ultimo elemento é ignorado
for cont in range(0,len(lanche)): # , para 2 argumentos do for # para cont no intervalo de 0 a "cumprimento" da tupla lanche, ou seja, vai até onde o len conta.
    print(lanche[cont]) #o lanche na posião 0 #vai comerçar em 0 que é o hambuguer
for pos, comida in enumerate(lanche):
    print(comida, pos)
print(sorted(lanche)) #sorted = organizado # transformou em uma lista para exibição

a = 1,5,8,2
b = 5,3,7
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5)) #quantas vezes aparece
print(d.index(3)) #posição, se tiver mais do mesmo objeto, vai aparecer na primeira incidencia 
print(c.index(5))
print(c.index(5,2)) #vai aparecer a posição do 5 a partir da posição 1. 

pessoa = "priscila",10,"limão",7
print(pessoa)
del(pessoa) #para excluir a pessoa

