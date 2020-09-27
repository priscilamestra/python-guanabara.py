# -*- coding: utf-8 -*-
print("Catetos e hipotenusa")

cat_op = float(input("Comprimento do cateto oposto:"))
cat_adj = float(input("Comprimento do cateto adjacente:"))
hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2) 
print("Hipotenusa = {:.2f}" .format(hip))

import math
co = float(input("cateto oposto:"))
ca = float(input("cateto adjacente:"))
hi = (math.hypot(co, ca))
print("hipotenusa: {:.2f}" .format(hi))

from math import hypot
co = float(input("cateto oposto:"))
ca = float(input("cateto adjacente:"))
hi = hypot(co, ca)
print("hipotenusa: {:.2f}" .format(hi))
