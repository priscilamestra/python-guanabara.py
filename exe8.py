# -*- coding: utf-8 -*-
print("Conversor de medidas")

medida = float(input("Digite uma distâcia em metros:"))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print("km =",km)
print("hm =", hm)
print("dam =",dam)
print("dm =",dm)
print("cm =" ,cm)
print("mm =" ,mm)

#menos linha de código:
#print("km = {}km \n hm = {}hm \n dam = {}dam \n dm = {}dm \n cm = {}cm \n mm = {}mm" .format(km,hm,dam,dm,cm,mm))

