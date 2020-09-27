print("Progressão aritmética")

primeiro = int(input("Primeiro valor:"))
razão = int(input("Razão:"))
décimo = primeiro + (10 - 1) * razão # (10-1) pq quero o décimo número
for i in range(primeiro, décimo + razão, razão): #(+ razão) para contar 10 valores
    print(i, end=" ")