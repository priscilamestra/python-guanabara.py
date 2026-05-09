print("Analisador completo.")
#F = fazer esse exercício de novo
soma = 0 
maior_id_homem = 0
nome_velho = "" #quando a resposta for uma str tem que usar o "" ao invés de 0
mulher_20 = 0
for i in range(1,4): #reptir as informações do laço dentro do intervalo solicitado
    print(f"----- {i}° PESSOA -----")
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
    print(f"Ao todo são {mulher_20} mulheres com menos de 20 anos.")
media = soma / i 
print(f"A média das idades analisadas é de {media:.2f}.")
print(f"O homem mais velho é {nome_velho} com {maior_id_homem} anos.")


# EXERCÍCIO 56 - ANALISADOR COMPLETO (VERSÃO 3)

soma_idade = 0
soma_pessoas = 0
idade_homem_mais_velho = 0
homem_mais_velho = ''
total_homens = 0 # A "chave" para a melhor prática
mulheres_abaixo_20 = 0
for pessoa in range(1,5):
  print("-----------")
  nome = str(input("Nome: ")).strip()
  idade = int(input("Idade: "))
  sexo = str(input("Sexo [M/F]: ")).strip().upper()
  
  soma_idade = soma_idade + idade
  soma_pessoas = soma_pessoas + 1
  
  # LÓGICA DO HOMEM MAIS VELHO
  if sexo == 'M':
    total_homens = total_homens + 1
		 
    if total_homens == 1: # Se for o PRIMEIRO HOMEM (independente de ser a pessoa 1 ou 4)
        idade_homem_mais_velho = idade
        homem_mais_velho = nome
    else:
      if idade > idade_homem_mais_velho: # Se não for o primeiro, eu comparo
          idade_homem_mais_velho = idade
          homem_mais_velho = nome
        
  if sexo in 'Ff' and idade < 20:
    mulheres_abaixo_20 = mulheres_abaixo_20 + 1

media_idade = soma_idade / soma_pessoas
if mulheres_abaixo_20 == 1:
	msg_mulher = 'mulher'
else:
	msg_mulher = 'mulheres'
print(f"A média de idade do grupo é de {media_idade:.2f} anos\nO homem mais velho tem {idade_homem_mais_velho} anos e se chama {homem_mais_velho}\nAo todo tem {mulheres_abaixo_20} {msg_mulher} com menos de 20 anos")

# EXERCÍCIO 56 - ANALISADOR COMPLETO (VERSÃO 4)
# Diminuir os if's aninhados (melhor prática) - usando o total_homens para inaugurar o homem mais velho

soma_idade = 0
soma_pessoas = 0
idade_homem_mais_velho = 0
homem_mais_velho = ''
total_homens = 0 # A "chave" para a melhor prática
mulheres_abaixo_20 = 0
for pessoa in range(1,5):
  print("-----------")
  nome = str(input("Nome: ")).strip()
  idade = int(input("Idade: "))
  sexo = str(input("Sexo [M/F]: ")).strip().upper()
  
  soma_idade = soma_idade + idade
  soma_pessoas = soma_pessoas + 1
  
  # LÓGICA DO HOMEM MAIS VELHO
  if sexo == 'M':
    if total_homens == 1 or idade > idade_homem_mais_velho:
      idade_homem_mais_velho = idade
      homem_mais_velho = nome
    
  if sexo == 'F' and idade < 20:
    mulheres_abaixo_20 += 1
        
media_idade = soma_idade / soma_pessoas

if mulheres_abaixo_20 == 1:
	msg_mulher = 'mulher'
else:
	msg_mulher = 'mulheres'
print(f"A média de idade do grupo é de {media_idade} anos\nO homem mais velho tem {idade_homem_mais_velho} anos e se chama {homem_mais_velho}\nAo todo tem {mulheres_abaixo_20} {msg_mulher} com menos de 20 anos")


