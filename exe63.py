print("Sequência de Fibonacci V.1")

n = int(input("Quantos termos você quer mostar?:"))
t1 = 0
t2 = 1
cont = 3 # começa no 3 pq já temos o primeiro e o segundo termo.
print("{} - {} " .format(t1,t2), end=" ")
while cont <= n:
    t3 = t1 + t2
    print("- {}" .format(t3), end =" ")
    t1 = t2
    t2 = t3
    cont = cont + 1 # caso não coloque cria um looping. 


