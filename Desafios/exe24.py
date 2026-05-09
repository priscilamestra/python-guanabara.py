# -*- coding: utf-8 -*-
print("Verificando as primeiras letras do texto")
cid = input("Em que cidade você nasceu ? ").strip()
print(cid[:5].upper() == "SANTO")

cefet = input("Em que faculdade você estuda? ").strip()
print(cefet[:6].upper() == "CEFET")

lixo = input("Onde você joga seu resíduo? ").strip()
print(lixo[:5].upper() == "LIXO")
