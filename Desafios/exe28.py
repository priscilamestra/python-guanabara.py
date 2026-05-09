# -*- coding: utf-8 -*-
print("Jogo da adivinhação v.1")
from random import randint
from time import sleep
#import playsound

print("Vou pensar em um número entre 0 a 3. Adivinhe qual é esse número.")
#lista = [0,1,2,3,4,5]
#pc = int(random.choice(lista)) 
pc = randint(0,3)
num = int(input("Em qual número eu pensei? "))
print("PROCESSANDO A INFORMAÇÃO")
sleep(2)
if pc == num:
    print(pc, "\nVocê ganhou! Parabéns mané. ")
    #playsound.playsound("exe021.mp3")
elif num > 3:
    print("Número inválido seu idiota!") 
elif num < 0:
    print("Número inválido seu idiota!")       
else:
    print(pc, "\nEu ganhei otário HAHAHAHA ")

 