print("Conversor de temperaturas")
celsius = float(input("Informe a temperatura em °C:"))
fahrenheit = float(input("Informe a temperatura em °F:"))
f = celsius * 1.8 + 32
c = (fahrenheit - celsius) / 1.8

print(f"A temperatura de {celsius:.2f}°C corresponde a {f:.2f}°F")
print(f"A temperatura de {fahrenheit:.2f}°F corresponde a {c:.2f}°C")
