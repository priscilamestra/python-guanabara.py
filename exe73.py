print("Tuplas com time de futebol")

times = "Flamengo", "Vasco", "Fluminense", "Botafogo", "Cabofriense", "Friburguense" #colocar a primeira letra maiscula em todos pra comparar igual
print(f"Os três primeiros times são {times[:3]}.")
print(f"Os que estão na zona de rebaixamento são {times[-2:]}") #se colocar [-2:-1] o ultimo não sai
print(f"Times em ordem alfabética: {sorted(times)}") #ordem alfabética
print(f"O Botafogo está na {(times.index('Botafogo')+1)}° posição.") #citação da tupla é com ' ' interpolação


