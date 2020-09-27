# -*- coding: utf-8 -*-
from math import cos, radians, sin, tan
print("sen, cos, tg")
ang = float(input(" ângulo:"))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print(" Sen = {:.2f} \n Cos ={:.2f} \n Tg = {:.2f}" .format(sen,cos,tg))
