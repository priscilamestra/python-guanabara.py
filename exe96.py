print("  Função que calcula área    ")

def area(larg,comp):
    a = larg * comp
    print(f"A área de um terreno {larg:.2f}x{comp:.2f} é {a:.2f}m²")

#programa principal
print("    Controle de terrenos    ")
print("-" * 40)
l = float(input("Largura (m):"))
c = float(input("Comprimento (m):"))
area(l,c)

    
    