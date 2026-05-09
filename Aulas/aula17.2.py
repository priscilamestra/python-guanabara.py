print("Aula 17 parte 2")

dados = []
dados.append("pedro")
dados.append(15)
pessoas = []
pessoas.append(dados[:]) # [para colocar um indice, uma posição] [:] gerar fatiamento da estrutura completa de dados. Gera uma cópia
print(pessoas[0][0]) #vai printar item 0 da lista maior e o item 0 da lista menor
galera = [["maria",19], ["joão",25]]
print(galera[1][0]) # vai printar só "joão"
for p in galera: #para cada pessoa em galera
    print(p)
    print(p[0]) # vai aparcer só os nomes
    print(p[1]) #vai aparecer só as idades
    print(f"{p[0]} tem {p[1]} anos.")
turma = []
inf = [] #estrutura auxiliar
totalmai = totalme = 0
for c in range(0,3):
    inf.append(input("nome:"))
    inf.append(int(input("idade:")))
    turma.append(inf[:]) #se não colocar o [:] não vai gerar uma cópia e sim uma ligação, logo se imprimir vai aparecer uma lista vazia pq a função clear vai apagar tudo
    inf.clear() #vai limpar a lista inf para o próximo usuário #apaga os dados toda vez que eu faço o laço #dados pra jogar dentro da galera
for p in turma: #para cada pessoa em turma analise se:
    if p[1] >= 18: #indice [1] representa a idade
        print(f"{p[0]} é maior de idade.")
        totalmai = totalmai + 1
    else:
        print(f"{p[0]} é menor de idade.")
        totalme = totalme + 1
if totalmai == 1 and totalme == 1:
    print(f"Temos {totalmai} maior de idade e {totalme} menor de idade.")
elif totalmai == 1 and totalme > 1:
    print(f"Temos {totalme} menores de idade e {totalmai} maior de idade.")
elif totalmai == 0 and totalme > 1:
    print(f"Temos nenhum maior de idade e {totalme} menores de idade.")
elif totalme == 1 and totalmai > 1:
    print(f"Temos {totalme} menor de idade e {totalmai} maiores de idade.")
elif totalme == 0 and totalmai > 1:
    print(f"Temos nenhum menor de idade e {totalmai} maiores de idade.")

