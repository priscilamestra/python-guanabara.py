print("É par ou ímpar?")

num = int(input("Me diga um número qualquer:"))
resultado = num % 2

if resultado == 1:
    print("O número {} é {}ímpar{}." .format(num, "\033[1;32m", "\033[m"))
else:
    print("O número {} é {}par{}." .format(num, "\033[1;32m", "\033[m"))