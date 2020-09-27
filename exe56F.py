print("Analisador completo.")
#F = fazer esse exercício de novo
soma = 0 
maior_id_homem = 0
nome_velho = "" #quando a resposta for uma str tem que usar o "" ao invés de 0
mulher_20 = 0
for i in range(1,4): #reptir as informações do laço dentro do intervalo solicitado
    print("----- {}° PESSOA -----" .format(i))
    nome = input("Nome:").strip().upper() #strip = tirar os espaços #upper = caixa alta
    idade = int(input("Idade:"))
    sexo = input("Sexo [M/F]:").upper().strip()
    soma = soma + idade # soma de todas as idades
    if i == 1 and sexo in "Mn": # o primeiro é o mais velho
        maior_id_homem = idade
        nome_velho = nome
    if sexo in "Mn" and idade > maior_id_homem: # se os outros forem maiores que o primeiro, vai ser substituido 
        maior_id_homem = idade
        nome_velho = nome  
    if sexo in "Ff" and idade < 20: # se for Ff e menor que 20 anos # variável in (receber) resposta 
        mulher_20 = mulher_20 + 1 # +1 conta a quantidade solicitada # td vez que tiver Ff menor que 20 vai contar
if mulher_20 == 1:
    print("Ao todo só tem 1 mulher com menos de 20 anos.")
if mulher_20 == 0:
    print("Nenhuma mulher tem menos de 20 anos")
if mulher_20 > 1:
    print("Ao todo são {} mulheres com menos de 20 anos." .format(mulher_20))
media = soma / i 
print("A média das idades analisadas é de {:.2f}." .format(media))
print("O homem mais velho é {} com {} anos." .format(nome_velho,maior_id_homem))



