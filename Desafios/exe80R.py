print("Lista ordenada sem reptições")

valores = []
for cont in range(0,5):
    n = int(input("Digite um número:"))
    if cont == 0 or n > valores[-1]: #se o contador estive na pos 0 ou n > que o ultimo valor digitado
        valores.append(n)
        print("Adicionado ao final da lista.")
    else: #entre o maior valor o e menor
        pos = 0 # para varrear todas as posições
        while pos < len(valores): #enquanto a posição for menor que o ultimo valor
            if n <= valores[pos]: #se n <= ao valor na posição
                valores.insert(pos, n) # vou inserir na posição o n
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos = pos + 1 # pra ele ir passando na posição
    #if n not in valores: 
        #valores.append(n)
        #print("Adicionado com sucesso.")
    #else:
        #while n in valores:
            #n = int(input("Valor já digitado, digite novamente:"))
        
#valores.sort()
print(valores)

