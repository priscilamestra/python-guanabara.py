# -*- coding: utf-8 -*-
print("Conversor de medidas")

medida = float(input("Digite uma distâcia em metros:"))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f"km = {km:.2f}")
print(f"hm = {hm:.2f}")
print(f"dam = {dam:.2f}")
print(f"dm = {dm:.2f}")
print(f"cm = {cm:.0f}")
print(f"mm = {mm:.0f}")

#menos linha de código:
#print("km = {}km \n hm = {}hm \n dam = {}dam \n dm = {}dm \n cm = {}cm \n mm = {}mm" .format(km,hm,dam,dm,cm,mm))

