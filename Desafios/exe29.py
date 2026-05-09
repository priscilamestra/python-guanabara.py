print("Radar eletrônico")

velo = float(input("Qual é a velocidade do carro em km/h?"))
multa = (velo - 80) * 7
multa2 = (25 - velo) * 7
print("--------------")
if velo > 80:
    print("\033[31m {:.2f}km/h \n MULTADO - você excedeu o limite permitido de 80km/h \n Multa no valor de R${:.2f}.\033[m \n Dirija com segurança!" .format(velo,multa))
elif velo < 25:
    print("\033[31m {:.2f}km/h \n MULTADO - você não cumpriu a velocidade mínima permitida de 25km/h \n Multa no valor de R${:.2f}.\033[m \n Dirija com segurança!" .format(velo,multa2))   
elif velo <= 80:
    print("\033[32m{}km/h \nTenha um bom dia, dirija com seguraça!\033[m" .format(velo))

print("-----------------")
if velo > 110:
    print(" {:.2f}km/h \nMULTADO - você excedeu o limite permitido de 80km/h \n Multa no valor de R${:.2f}. \n Dirija com segurança!" .format(velo,multa))
print("DETRAN agradece!")    