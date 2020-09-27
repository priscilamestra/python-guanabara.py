print("Analisando triângulo")

r1 = float(input("Primeiro seguimento:"))
r2 = float(input("Segundo seguimento:"))
r3 = float(input("Terceiro seguimento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima {}PODEM{} formar um triângulo." .format("\033[1;32m", "\033[m")) 
else:
    print("Os seguimentos acima {}NÃO PODEM{} formar um triângulo." .format("\033[1;31m", "\033[m")) 