print("número por extenso")
cont = "zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez"
while True:
    num = int(input("Digite um número de 0 a 10: "))
    while num < 0 or num > 10:
        num = int(input("Número inválido, digite um número de 0 a 10:"))
    print(f"Você digitou o número {cont[num]}.") #variável cont na posição num #posição é com []
    resposta = input("Você deseja continuar? [S/N]:").strip().upper()[0]
    while resposta not in "SN":
        resposta = input("Resposta inválida. Você deseja continuar? [S/N]:").strip().upper()[0]
    if resposta == "N":
        break

