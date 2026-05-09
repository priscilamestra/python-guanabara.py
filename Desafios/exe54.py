from datetime import date
print("Grupo da maioridade")

atual = date.today().year
maior = 0
menor = 0
for i in range(1,4):
    ano = int(input("Em que ano a {}° pessoa nasceu?" .format(i)))
    idade = atual - ano
    if idade >= 18:
        maior = maior + 1 # contador, a cada 1 que se enquadra no if vai ser acrescentado.
    else:
        menor = menor + 1
if maior == 1 or maior ==0:
    print(f"Ao todo tivemos {maior} maior de idade.") #fora do laço pra não reptir a cada frase
else:
    print(f"Ao todo tivemos {maior} maiores de idade.") #fora do laço pra não reptir a cada frase

if menor == 1 or menor == 0:
    print(f"E também tivemos {menor} menor de idade.")
else:
    print(f"E também tivemos {menor} menores de idade.")
# usei outros if para ter concordância verbal na resposta.


# EXERCÍCIO 54 - GRUPO DA MAIORIDADE (VERSÃO 3)
from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 4):
  nascimento = int(input(f"Em que ano a {pessoa}° pessoa nasceu? "))
  idade = ano_atual - nascimento
  if idade >= 18:
    total_maior = total_maior + 1
  else:
    total_menor = total_menor + 1
# Lógica para o texto da maioridade    
if total_maior == 1:
  txt_maior = "pessoa maior"
else:
  txt_maior = "pessoas maiores"
# Lógica para o texto da menoridade	
if total_menor == 1:
  txt_menor = "pessoa menor"
else:
  txt_menor = "pessoas menores"

print(f"Ao todo tivemos {total_maior} {txt_maior} de idade e {total_menor} {txt_menor} de idade")


