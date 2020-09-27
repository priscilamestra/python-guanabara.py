print("Aula 18")

dados = dict()
dados = {'nome':'pedro', 'idade':25} #nome = indentificador do elemento, pedro = valor # idade = id do elemento, 25 = valor
print(dados['nome']) #[] nome é um indice
dados['sexo'] = 'M' #append não funciona aqui, ou seja automaticamente ele vai criar mais um indice e um valor
#del dados['indice que você quer deletar'] (del é separado mesmo)
filme = {
    'titulo':'star wars','ano':1977,'diretor':'George lucas'
}
#metodos:
print(filme.values()) #values (valores)= star wars, 1977, george lucas
print(filme.keys()) #keys (chaves) = titulo, ano, diretor
print(filme.items()) #items (itens) = valores + chaves

for k,v in filme.items():
    print(f"O {k} é {v}.") # O titulo é star wars, o ano é 1977, o diretor é george lucas.

pessoas = {'nome':'priscila','idade':25}
pessoas ['peso'] = 70 # vai adicionar chave: peso, valor: 70
pessoas ['nome'] = 'pri' # vai substituir priscila
print(pessoas['nome'])
for k in pessoas.keys():
    print(k) # vai mostrar as chaves: nome e idade
for k, v in pessoas.items():
    print(f'{k} = {v}')

teste = {'nome': 'maria', 'sexo': 'F'}
del teste['sexo']
print(teste) 

#dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) # vai mostrar uma lista com dois dicionários
print(brasil[0]['uf']) #vai mostrar rio de janeiro

estado = {}
brasil1 = []
for c in range(0, 2): # para cada contador no intervalo de 0,2 ( ou seja, os 2 inputs vão se reptir 2 vezes)
    estado['uf'] = input("Unidade federativa:")
    estado['sigla'] = input("Sigla:")
    brasil1.append(estado.copy()) # fateamento não funciona aqui, existe um metodo interno (.copy)
for e in brasil1: #para cada estado em brasil 
    for k, v in e.items(): #para cada estado em brasil e para cada chave e valor em estado:
        print(f"{k} = {v}.") #uf = rio, sigla = rj, uf = sampa, sigla = sp


