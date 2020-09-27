print("Um print especial")

def escrita(txt):
    print("-" * len(txt))
    print(txt)
    print("-" * len(txt))

#programa principal
escrita("Python developer")    
escrita("tech woman")

def frase(msg):
    tam = len(msg) + 4 #(bordinha)
    print("-" * tam)
    print(f"  {msg}") #centralizar as bordas
    print("-" * tam)

#programa principal
frase("Olá mundo")
frase("programadora python")