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


