print("Grupo da maioridade")

from datetime import date 
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
    print("Ao todo tivemos {} maior de idade." .format(maior)) #fora do laço pra não reptir a cada frase
else:
    print("Ao todo tivemos {} maiores de idade." .format(maior)) #fora do laço pra não reptir a cada frase

if menor == 1 or menor == 0:
    print("E também tivemos {} menor de idade." .format(menor))
else:
    print("E também tivemos {} menores de idade." .format(menor))
# usei outros if para ter concordância verbal na resposta.


