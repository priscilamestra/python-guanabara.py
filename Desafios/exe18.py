# -*- coding: utf-8 -*-
from math import cos, radians, sin, tan

angulo = float(input("Digite o ângulo que você deseja: "))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))

print(f"Seno = {sen:.2f} \nCosseno = {cos:.2f} \nTangente = {tg:.2f}")