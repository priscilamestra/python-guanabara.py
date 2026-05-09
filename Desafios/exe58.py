print("Jogo da adivinhaão V.2")
from random import randrange
from time import sleep 
pc = randrange(0,11)

print("""Olá, sou seu computador ACER guerreiro de 2020,
E acabei de pensar em um número de 0 a 10.
Será que você consegue adivinar ?!""")
num = int(input("Qual seu palpite?"))
cont = 0
while num < 0 or num > 10: #tratamento de erro para qd o usuário digitar str aparecer msg de erro
    num = int(input("Número fora do intervalo, digite um número entre 0 e 10:"))
print("PROCESSANDO A INFORMAÇÃO")
sleep(1)
while not pc == num:
    if num > pc:
        num = int(input("Dica: menos mozão. Tenta de novo:"))
    else:
        num = int(input("Dica: mais paixão. Tenta de novo:"))
    cont = cont + 1    
if pc == num:
    print("Você ganhou porque eu deixei, ok?!")
else:
    print("GANHEEEEI MANÉ") 
print("Você precisou jogar {} vezes pra me vencer." .format(cont))