# -*- coding: utf-8 -*-
print("Conversor de temperaturas")
celsius = float(input("Informe a temperatura em °C:"))
fahrenheit = float(input("Informe a temperatura em °F:"))
f = celsius * 1.8 + 32
c = (fahrenheit - celsius) / 1.8


print("A temperatura de {:.2f}°C corresponde a {:.2f}°F" .format(celsius,f))
print("A temperatura de {:.2f}°F corresponde a {:.2f}°C" .format(fahrenheit,c))