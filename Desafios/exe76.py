print("Lista de preços com tupla.")
listagem = "Lápis", 1.50, "Borracha", 2.50, "caderno", 20.00, "Estojo", 15.00,"Mochila", 40.00
print(listagem)
print("-" * 40)
print("Jeito atualizado de centralizar".center(40))
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
for i in listagem: #teste de tipagem 
    if type(i) is str:
        print(f"{i:.<30}", end = ' ')
    else:
        print(f"R${i:>5.2f}") 
print("-" * 40)       

#outro jeito de fazer
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end = ' ') #[] indice pos 
    else:
        print(f"R${listagem[pos]:>5.2f}")
