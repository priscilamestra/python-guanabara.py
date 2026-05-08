# -*- coding: utf-8 -*-
#V1
cat_op = float(input("Comprimento do cateto oposto:"))
cat_adj = float(input("Comprimento do cateto adjacente:"))
hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2) 
print(f"Hipotenusa = {hip:.2f}")

#V2
import math  # noqa: E402
co = float(input("cateto oposto:"))
ca = float(input("cateto adjacente:"))
hi = (math.hypot(co, ca))
print(f"hipotenusa: {hi:.2f}")

#V3
from math import hypot  # noqa: E402
co = float(input("cateto oposto:"))
ca = float(input("cateto adjacente:"))
hi = hypot(co, ca)
print(f"hipotenusa: {hi:.2f}")
