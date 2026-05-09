try:
    import importlib
    emoji = importlib.import_module("emoji")
    EMOJI_AVAILABLE = True
except ImportError:
    emoji = None
    EMOJI_AVAILABLE = False
import math

if EMOJI_AVAILABLE:
    print(emoji.emojize("olá :sunglasses:"))
else:
    print("olá 😎")
num = int(input("digite um numero:"))
raiz = math.sqrt(num)
print(math.ceil(raiz)) #arredondar para cima
print(math.floor(raiz)) #arredondar para baixo
print(math.e) #numero de euler
print(math.pi)

import random # o programa escolhe um num aleatorio  # noqa: E402
num = random.randint(0,1000) #argumento a e b
print(num)







