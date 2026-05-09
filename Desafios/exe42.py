print("Analisando triângulo v.2")

r1 = float(input("Digite o primeiro segmento:"))
r2 = float(input("Digite o segundo segmento:"))
r3 = float(input("Digite o terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima {}PODEM{} formar um triângulo " .format("\033[1;32m", "\033[m") , end="") 
    if r1 == r2 == r3:
        print("\033[1mEQUILÁTERO.\033[m")
    elif r1 != r2 != r3 != r1:
        print("\033[1mESCALENO.\033[m")
    else:
        print("\033[1mISÓCELES.\033[m")   

else:
    print("Os seguimentos acima {}NÃO PODEM{} formar um triângulo." .format("\033[1;31m", "\033[m")) 

