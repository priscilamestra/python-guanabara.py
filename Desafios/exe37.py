print("Conversor de bases numéricas")

num = int(input("Digite um número inteiro:"))
print("Escolha umas das bases para conversão:")
print("[1] converter para \033[1mBinário\033[m")
print("[2] converter para \033[1mOctal\033[m")
print("[3] converter para \033[1mHexadecimal\033[m")
opçao = int(input("Sua opção:"))
while opçao < 1 or opçao > 3:
    opçao = int(input("Opção inválida, por favor digite novamente:"))
if opçao == 1:
    num = bin(num)[2:] #0b
    print("Binário =", num)
elif opçao == 2:
    num = oct(num)[2:] #0o #[2:] fatiamento de uma str, ou seja, vai retirar as 2 primeiras "letras"
    print("Octal =", num)
elif opçao == 3:
    num = hex(num)[2:] #0x
    print("Hexadecimal =", num)

