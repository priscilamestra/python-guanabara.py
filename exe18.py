# -*- coding: utf-8 -*-
from math import cos, radians, sin, tan
print("sen, cos, tg")
ang = float(input(" ângulo:"))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print(f"Sen = {sen:.2f} \n Cos = {cos:.2f} \n Tg = {tg:.2f}")